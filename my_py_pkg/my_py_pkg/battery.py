#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
 
 
class BatteryClient(Node): 
    def __init__(self):
        super().__init__("battery_client")
        self.battery_full = True
        self.client_ = self.create_client(SetLed, "set_led") 
        self.timer_ = self.create_timer(1.0, self.battery_callback)

    def battery_callback(self):
        if self.battery_full:
            # Battery just became empty
            self.battery_full = False
            self.get_logger().info("Battery empty! Turning LED ON")
            self.call_set_led(0, 1)
            
            # Change timer to 6 seconds (time until full)
            self.timer_.cancel()
            self.timer_ = self.create_timer(6.0, self.battery_callback)
        else:
            # Battery just became full
            self.battery_full = True
            self.get_logger().info("Battery full! Turning LED OFF")
            self.call_set_led(0, 0)
            
            # Change timer to 4 seconds (time until empty)
            self.timer_.cancel()
            self.timer_ = self.create_timer(4.0, self.battery_callback)

    def call_set_led(self, led_number, state):
        while not self.client_.wait_for_service(1.0): #Timeout in 1 secs
            self.get_logger().warning("Waiting for Led Panel Server")
        
        request = SetLed.Request()
        request.led_number = led_number
        request.state = state

        future = self.client_.call_async(request)
        future.add_done_callback(self.callback_set_led) 

    def callback_set_led(self, future):
        response = future.result()
        self.get_logger().info(f"LED update success: {response.success}")
 
 
def main(args=None):
    rclpy.init(args=args)
    node = BatteryClient() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()

#LED panel and Battery