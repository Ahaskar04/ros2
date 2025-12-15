#!/user/bin/env python3
import rclpy #python library for ros 2
from rclpy.node import Node

class MyNode(Node): #passes the main Node class

    def __init__(self):
        super().__init__("py_test") #creates a Node
        self.get_logger().info("Hello World")


def main(args=None):
    rclpy.init(args=args) #initialize ros 2 communication
    node = MyNode() #creating the node using our own class MyNode
    rclpy.spin(node) #keeps the node alive
    rclpy.shutdown() # close ros 2 communication

if __name__ == "__main__":
    main()
