#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import threading
import tkinter as tk

class Node1(Node):
    def __init__(self):
        super().__init__('node1')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        # Start UI in a new thread so it doesn't block the ROS event loop
        ui_thread = threading.Thread(target=self.init_ui)
        ui_thread.daemon = True
        ui_thread.start()

    def on_button_click(self):
        msg = String()
        msg.data = ' 🟢 Button clicked!'
        self.publisher_.publish(msg)
        #self.get_logger().info('🟢 Button was clicked — Published: "Button clicked!"')

    def init_ui(self):
        root = tk.Tk()
        root.title("Node1 UI")

        button = tk.Button(root, text="Send Message", command=self.on_button_click, padx=20, pady=10)
        button.pack(pady=20)

        root.mainloop()

def main(args=None):
    rclpy.init(args=args)
    node = Node1()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
