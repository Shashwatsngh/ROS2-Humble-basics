ROS 2 Workspace: TurtleSim Control
Overview

This repository contains a ROS 2 workspace with various nodes written in Python to interact with the turtlesim simulation. The nodes are designed to publish commands, subscribe to topics, and utilize services to control the turtle's behavior.

Node Descriptions

draw_circle.py
        Purpose: Publishes velocity commands to make the turtle move in a circular path.
        Topics Published:
            /turtle1/cmd_vel (geometry_msgs/Twist): Sends linear and angular velocities.
        Key Features:
            Publishes commands at regular intervals to maintain a circular motion.

my_first_node.py
        Purpose: A basic example node that logs a counter value at regular intervals.
        Key Features:
            Demonstrates simple ROS 2 node structure and timer usage.
            Logs incrementing counter values to the console.

pose_subscriber.py
        Purpose: Subscribes to the turtle's pose and logs its position.
        Topics Subscribed:
            /turtle1/pose (turtlesim/Pose): Receives the turtle's pose information (x, y, orientation).
        Key Features:
            Logs the turtle's position (x, y) whenever it changes.

turtle_controller.py
        Purpose: Combines subscription, publication, and service usage to control the turtle's movement and pen color dynamically.
        Topics Published:
            /turtle1/cmd_vel (geometry_msgs/Twist): Controls turtle's speed and direction.
        Topics Subscribed:
            /turtle1/pose (turtlesim/Pose): Monitors turtle's position.
        Services Used:
            /turtle1/set_pen (turtlesim/srv/SetPen): Changes the turtle's pen color dynamically.
        Key Features:
            Adjusts velocity based on the turtle's position.
            Changes pen color between red and blue when crossing x = 5.5.
