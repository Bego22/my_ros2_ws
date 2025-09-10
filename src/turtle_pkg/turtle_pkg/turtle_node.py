#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

class TurtleKeyController(Node):
    def __init__(self):
       super().__init__("turtle_node")
       self.pub_node1 = self.create_publisher(Twist , '/turtle1/cmd_vel' , 10)
       self.pub_node2 = self.create_publisher(Twist , '/turtle2/cmd_vel' , 10)
       
       self.listener = keyboard.Listener(on_press=self.on_press)
       self.listener.start()

    def on_press(self , key):
        msg1 = Twist()
        msg2 = Twist()
        try :
            if key.char == 'w' :
               msg1.linear.x = 1.0
               msg1.angular.z = 0.0
            elif key.char == 's' :
               msg1.linear.x = -1.0
               msg1.angular.z = 0.0
            elif key.char == 'a' :
               msg1.linear.x = 0.0
               msg1.angular.z = 1.0
            elif key.char == 'd' :
               msg1.linear.x = 0.0
               msg1.angular.z = - 1.0
            self.get_logger().info(f"You Entered {key}")
        except AttributeError:
            if key == keyboard.Key.up:
                msg2.linear.x = 1.0
                msg2.angular.z = 0.0
            elif key == keyboard.Key.down:
                msg2.linear.x = -1.0
                msg2.angular.z = 0.0
            elif key == keyboard.Key.left:
                msg2.linear.x = 0.0
                msg2.angular.z = 1.0
            elif key == keyboard.Key.right:
                msg2.linear.x = 0.0
                msg2.angular.z = - 1.0
            self.get_logger().info(f"You Entered {key}")
        self.pub_node1.publish(msg2)
        self.pub_node2.publish(msg1)
        
        
def main():
    
    rclpy.init()
    node = TurtleKeyController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
