#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64 
 
class NumberNode(Node): 
    def __init__(self):
        super().__init__("number")
        self.declare_parameter("number", 2)
        self.declare_parameter("time_period", 1.0)
        self.number_ = self.get_parameter("number").value
        self.timer_value_ = self.get_parameter("time_period").value
        self.publisher_ = self.create_publisher(Int64, "number", 10) 
        self.timer_ = self.create_timer(self.timer_value_, self.publish_number)
        self.get_logger().info("Robot News Station has been started")

    def publish_number(self):
        msg=Int64()
        msg.data=self.number_
        self.publisher_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()