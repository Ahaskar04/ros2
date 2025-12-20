#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
 
class LetPanelNode(Node): 
    def __init__(self):
        self.state = [0,0,0]
        super().__init__("led_panel") 
        self.server_ = self.create_service(SetLed, "set_led", self.callback_set_led)
        self.get_logger().info("Set Led server has been started")

    def callback_set_led(self, request:SetLed.Request, response:SetLed.Response):
        self.state[request.led_number] = request.state
        response.success = True
        return response
 
 
def main(args=None):
    rclpy.init(args=args)
    node = LetPanelNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
#Server