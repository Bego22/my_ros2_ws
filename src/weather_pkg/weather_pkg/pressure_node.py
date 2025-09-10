#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import FluidPressure
import random

class timer_node(Node):
    def __init__(self):
        super().__init__("pressure_node")
        self.get_logger().info("Pressure_Node Started")
        self.publisher_node = self.create_publisher(FluidPressure ,"/pressure",10)
        self.create_timer(3,self.timer_callback)
        
    def timer_callback(self):
        msg = FluidPressure()
        msg.fluid_pressure = float(random.randint(900 , 1100))
        self.get_logger().info("Pressure sent")
        self.publisher_node.publish(msg)
        


def main():
    rclpy.init()
    node = timer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()