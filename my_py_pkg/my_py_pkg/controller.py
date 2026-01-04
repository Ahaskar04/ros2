#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import TurtleArray  
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class controller(Node):
    def __init__(self):
        super().__init__("controller")
        self.turtle1_pose_ = None
        self.target_turtle_ = None
        self.smallest_distance = float('inf')
        self.turtle_list_sub_ = self.create_subscription(
            TurtleArray, "turtle_list", self.callback_turtle_list, 10)
        self.pose_sub_ = self.create_subscription(
            Pose, "/turtle1/pose", self.callback_pose, 10
        )
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(0.1, self.call_cmd_vel)
    
    def callback_pose(self, msg):
        self.turtle1_pose_ = msg

    def callback_turtle_list(self, msg):
        if self.turtle1_pose_ is None:
            return
        
        if self.target_turtle_ is None:
            for turtle in msg.turtles:
                distance = math.sqrt(
                    math.pow(self.turtle1_pose_.x - turtle.x, 2) + 
                    math.pow(self.turtle1_pose_.y - turtle.y, 2))
                if distance < self.smallest_distance:
                    self.smallest_distance = distance
                    self.target_turtle_ = turtle

    def call_cmd_vel(self):
        if self.target_turtle_ is None or self.turtle1_pose_ is None:
            return
        
        distance = math.sqrt(
            math.pow(self.turtle1_pose_.x - self.target_turtle_.x, 2) + 
            math.pow(self.turtle1_pose_.y - self.target_turtle_.y, 2))
        
        self.get_logger().info(f"Distance to target: {distance}")
        
        if distance < 0.5:  
            self.get_logger().info("Caught!")
            self.target_turtle_ = None
            self.smallest_distance = float('inf')  
            # TODO: call kill service here later
            return
    
        msg = Twist()
        angle_to_target = math.atan2(
            self.target_turtle_.y - self.turtle1_pose_.y,   
            self.target_turtle_.x - self.turtle1_pose_.x)
        angle_diff = angle_to_target - self.turtle1_pose_.theta
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        msg.linear.x = distance * 0.2
        msg.angular.z = angle_diff  * 2.0 # turn toward target
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = controller()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()