#!/user/bin/env python3
import rclpy #python library for ros 2
from rclpy.node import Node

class MyNode(Node): #passes the main Node class

    def __init__(self):
        super().__init__("py_test") #creates a Node named py_test
        self.counter_ = 0 #counter is in the class, can be used in any other functions of the class
        self.get_logger().info("Hello World")
        self.create_timer(1.0, self.timer_callback) #we do not want to call the function, we're just registering the function

    def timer_callback(self):
        self.get_logger().info("Hello" + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args) #initialize ros 2 communication
    node = MyNode() #creating the node using our own class MyNode
    rclpy.spin(node) #keeps the node alive
    rclpy.shutdown() # close ros 2 communication

if __name__ == "__main__":
    main()
