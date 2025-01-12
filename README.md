# ROS2 Turtlesim Projects

This repository showcases different **ROS2** projects that I worked on using the **Turtlesim** simulator. The projects demonstrate basic functionalities and control techniques with ROS2.

---

## **Projects and Videos**

### **1. ROS2 Service Basics Using Turtlesim (Pen Changes Colour When Passing the Centerline)**

This project demonstrates the use of a **ROS2 service** to change the turtle's pen color when it crosses the centerline of the Turtlesim window. The pen turns red as the turtle crosses the centerline and blue as it returns.

[![Watch the video](https://img.youtube.com/vi/PlLu4rXfTjE/0.jpg)](https://www.youtube.com/watch?v=PlLu4rXfTjE)

---

### **2. ROS2 Humble Draw Circle with Turtlesim**

This project shows how to command the turtle to draw a circle using **ROS2**. It publishes velocity commands that make the turtle move in a circular path.

[![Watch the video](https://img.youtube.com/vi/NjtXWxMJvs0/0.jpg)](https://youtu.be/NjtXWxMJvs0?si=ge2xAxgkIcD4_bz5)

---

### **3. ROS2 Humble Closed Loop Turtlesim (Turtle Never Crosses the Walls and Changes Trajectory)**

In this project, the turtle moves in such a way that it never crosses the boundaries of the Turtlesim window. A **closed-loop control** mechanism adjusts its trajectory to avoid collisions with the walls.

[![Watch the video](https://img.youtube.com/vi/k-R5tH_NORE/0.jpg)](https://youtu.be/k-R5tH_NORE?si=jdxb5JWMXkfDjP5s)

---

## **Explanation of Python Files**

### **draw_circle.py**

This file contains a ROS2 node that sends velocity commands to the turtle, making it move in a circular path using linear and angular velocities.

---

### **my_first_node.py**

This file demonstrates a simple ROS2 node that logs a counter value every second. It introduces basic functionality of creating and handling timers in ROS2.

---

### **pose_subscriber.py**

This file subscribes to the turtle's pose topic and logs its current x and y coordinates. It helps demonstrate the subscription mechanism in ROS2.

---

### **turtle_controller.py**

This file controls the turtle’s movement based on its position. The turtle adjusts its trajectory when it nears the boundaries and changes its pen color based on crossing a certain x-coordinate.

---
