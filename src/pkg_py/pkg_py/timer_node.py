#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

class timer_node(Node):
    def __init__(self):
        super().__init__("timer_node")
        self.get_logger().info("Timer_Node Started")
        self.counter = 10
        self.timer = self.create_timer(1, self.callback)
    def callback(self):
        if self.counter >= 0 :
            self.get_logger().info(f" {self.counter} ")
            self.counter -= 1
        else :
            self.get_logger().info("Time is up!")
            self.timer.cancel() # End message printed only one time by this line 


def main():
    rclpy.init()
    node = timer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()