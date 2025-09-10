#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import RelativeHumidity
from sensor_msgs.msg import Temperature
from sensor_msgs.msg import FluidPressure
from pathlib import Path

class timer_node(Node):
    def __init__(self):
        super().__init__("monitor_node")
        self.get_logger().info("Monitor_Node Started")
        self.temp = 0 
        self.press = 0 
        self.hum = 0
        self.sub_node1 = self.create_subscription(Temperature , "/temperature" , self.temp_callback , 10)
        self.sub_node2 = self.create_subscription(RelativeHumidity ,"/humidity" , self.hum_callback , 10)
        self.sub_node3 = self.create_subscription(FluidPressure , "/pressure" , self.press_callback ,10)

        self.create_timer(1,self.callback)
        
    def temp_callback(self,msg):
        self.temp = msg.temperature
    def hum_callback(self,msg):
        self.hum = msg.relative_humidity
    def press_callback(self,msg):
        self.press = msg.fluid_pressure
    def callback (self):
        self.get_logger().info(f"Temp = {int(self.temp)} ◦ C, Humidity = {int(self.hum)} %, Pressure = {int(self.press)} hPa.")
        with open("monitor.txt","a") as file :
            file.write(f"Temp = {int(self.temp)} ◦ C, Humidity = {int(self.hum)} %, Pressure = {int(self.press)} hPa.\n")



        


def main():
    rclpy.init()
    node = timer_node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()