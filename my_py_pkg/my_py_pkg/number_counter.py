#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter") 
        self.counter = 0
        self.subscriber_ = self.create_subscription(
            Int64, "number", self.callback_number_counter, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.get_logger().info("Number counter has been started")
        self.server_ = self.create_service(SetBool, "add_two_ints", self.callback_counter_reset)

    def callback_number_counter(self, msg: Int64):
        self.counter += msg.data
        
        count_msg = Int64()
        count_msg.data = self.counter
        self.publisher_.publish(count_msg)
        
        self.get_logger().info(f"Received {msg.data}, counter: {self.counter}")

    def callback_counter_reset(self, request:SetBool.Request, response: SetBool.Response):
        self.counter = request.data
        response.success = True
        response.message = "Success: Counter updated"
        return response


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()     
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()