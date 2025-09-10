#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import RelativeHumidity
import random


class timer_node(Node):
    def __init__(self):
        super().__init__("humidity_node")
        self.get_logger().info("Humidity_Node Started")
        self.publisher_node = self.create_publisher(RelativeHumidity ,"/humidity",10)
        self.create_timer(2,self.timer_callback)
        
    def timer_callback(self):
        msg = RelativeHumidity()
        msg.relative_humidity = float(random.randint(20 , 100))
        self.get_logger().info("Humidity sent")
        self.publisher_node.publish(msg)
        


def main():
    rclpy.init()
    node = timer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()