#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.action import CountUntil
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
import time


class CountUntilServerNode(Node):#Modify name of the class
    def __init__(self):
        super().__init__("count_until_server") #modify name of the node
        self.count_until_server_ = ActionServer(self,CountUntil, 
                                                "count_until", 
                                                execute_callback=self.execute_callback)
        # self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Count Until Server has been started")

    # def timer_callback(self):
    #         self.get_logger().info('Hello'+str(self.counter))
    #         self.counter += 1


    def execute_callback(self,goal_handle:ServerGoalHandle):
        #Get request fromm goal
        target_number = goal_handle.request.target_number
        period = goal_handle.request.period

        #Execute the action
        self.get_logger().info("Executing goal...")
        counter = 0
        for i in range(target_number):
            counter+=1
            self.get_logger().info(str(counter))
            time.sleep(period)
        
        #once done set goal final state
        goal_handle.succeed()

        #and send the result
        result = CountUntil.Result()
        result.reached_number = counter
        return result

    

def main(args=None):
    rclpy.init(args=args)
    node = CountUntilServerNode()  #Modify name of the class
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
