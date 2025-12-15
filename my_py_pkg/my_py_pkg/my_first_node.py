#!/user/bin/env python3
import rclpy #python library for ros 2
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args) #initialize ros 2 communication
    node = Node("py_test")
    node.get_logger().info("Hello World")
    rclpy.spin(node) #keeps the node alive
    rclpy.shutdown() # close ros 2 communication

if __name__ == "__main__":
    main()
