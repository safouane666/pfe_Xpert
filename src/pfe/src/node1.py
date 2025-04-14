#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.timer = self.create_timer(1.0, self.publish_msg)

    def publish_msg(self):
        msg = String()
        msg.data = 'Hello I am node1'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

    def listener_callback(self, msg):
        self.get_logger().info(f'Node1 heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
