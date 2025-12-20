#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedPanelState


class LedPanelNode(Node): 
    def __init__(self):
        super().__init__("led_panel")
        self.state = [0, 0, 0]
        
        # Service server
        self.server_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        
        # Publisher
        self.publisher_ = self.create_publisher(LedPanelState, "led_panel_state", 10)
        self.timer_ = self.create_timer(1.0, self.publish_led_state)
        
        self.get_logger().info("LED Panel has been started")

    def publish_led_state(self):
        msg = LedPanelState()
        msg.led_states = self.state
        self.publisher_.publish(msg)

    def callback_set_led(self, request: SetLed.Request, response: SetLed.Response):
        self.state[request.led_number] = request.state
        response.success = True
        self.get_logger().info(f"LED {request.led_number} set to {request.state}. State: {self.state}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

#LED panel and Battery