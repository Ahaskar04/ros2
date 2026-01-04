#!/usr/bin/env python3

# Client for /spawn service (calls it to create turtles)
# Publisher for your alive turtles topic (sends out TurtleArray)

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
import random
from my_robot_interfaces.msg import Turtle
from my_robot_interfaces.msg import TurtleArray  

class spawner(Node):
    def __init__(self):
        super().__init__("spawner")
        self.alive_turtles_ = []
        self.client_ = self.create_client(Spawn, "/spawn")
        self.turtle_list_pub_ = self.create_publisher(TurtleArray, "turtle_list", 10)
        self.timer_ = self.create_timer(3.0, self.call_spawn)

    def call_spawn(self):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warning("Waiting for the spawner server")

        request = Spawn.Request()
        request.x = random.uniform(1.0, 10.0)
        request.y = random.uniform(1.0, 10.0)
        request.theta = random.uniform(0, 2 * 3.14159)

        self.pending_x_ = request.x
        self.pending_y_ = request.y
        
        future = self.client_.call_async(request)
        future.add_done_callback(self.callback_spawn)

    def callback_spawn(self, future):
        new_turtle = Turtle()
        response = future.result()
        self.get_logger().info("Spawned: " + response.name)
        new_turtle.name = response.name
        new_turtle.x = self.pending_x_
        new_turtle.y = self.pending_y_
        self.alive_turtles_.append(new_turtle)

        msg = TurtleArray()
        msg.turtles = self.alive_turtles_
        self.turtle_list_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = spawner()
    node.call_spawn()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()