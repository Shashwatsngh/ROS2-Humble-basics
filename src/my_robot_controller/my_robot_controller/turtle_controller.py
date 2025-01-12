#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial


class turtle_control(Node):
    def __init__(self):
        self.previous_x_=0.0
        super().__init__("turtle_controller")
        self.cmd_vel_publisher_=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.pose_subscriber_=self.create_subscription(Pose,"turtle1/pose",self.pose_callback,10)
        self.get_logger().info("Turtle Controller Node has been started")

    def pose_callback(self,pose:Pose):
        cmd=Twist()
        if pose.x>9.0 or pose.x<2.0 or pose.y>9.0 or pose.y<2.0:
            cmd.linear.x=1.0
            cmd.angular.z=0.9
        else:
            cmd.linear.x=5.0
            cmd.angular.z=0.0
        self.cmd_vel_publisher_.publish(cmd)

        if pose.x>5.5 and self.previous_x_<=5.5:
            self.previous_x_=pose.x
            self.call_set_pen_service(255,0,0,3,0)
            self.get_logger().info("Red")

        elif pose.x<=5.5 and self.previous_x_>5.5:
            self.previous_x_=pose.x
            self.get_logger().info("Blue")
            self.call_set_pen_service(0,0,255,2,0)
        


    def call_set_pen_service(self,r,g,b,width,off):
        client = self.create_client(SetPen, 'turtle1/set_pen')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self,future):
        try:
            response = future.result()
            
        except Exception as e:
            self.get_logger().info('Service call failed %r' % (e,))   


def main(args=None):
    rclpy.init(args=args)
    node =turtle_control()
    rclpy.spin(node)
    rclpy.shutdown()