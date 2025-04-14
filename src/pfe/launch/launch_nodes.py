from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pfe',
            executable='node1',
            name='node1',
            output='screen'
        ),
        Node(
            package='pfe',
            executable='node2',
            name='node2',
            output='screen'
        ),
    ])
