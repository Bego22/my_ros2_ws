#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Temperature
import random 

class timer_node(Node):
    def __init__(self):
        super().__init__("temperature_node")
        self.get_logger().info("Temperature_Node Started")
        self.publisher_node = self.create_publisher(Temperature,"/temperature",10)
        self.create_timer(1,self.timer_callback)
        
    def timer_callback(self):
        msg = Temperature()
        msg.temperature = float(random.randint(15, 40))
        self.get_logger().info("Temperature sent")
        self.publisher_node.publish(msg)


def main():
    rclpy.init()
    node = timer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()