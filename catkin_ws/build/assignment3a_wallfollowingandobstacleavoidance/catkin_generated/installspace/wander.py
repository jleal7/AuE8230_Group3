#!/usr/bin/env python3

import numpy as np
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


#class obstacleAvoidance():
#def __init__(self):
        
#initializing the node

inds2 = [];
def callback(msg):

        #inds = np.where(msg.ranges == 0.0)[0]
        for i in range(len(msg.ranges)):
            if msg.ranges[i] == 0.0:
                ind2.append(msg.ranges[i])

        print(inds)
        #msg.ranges[inds] = 20
        msg.ranges[ind2] = 20
        
        print('Range at 0 degress: {}'.format(msg.ranges[0]))
        print('Range at 30 degress: {}'.format(msg.ranges[30]))
        print('Range at 330 degress: {}'.format(msg.ranges[330]))
        print('Range at 90 degress: {}'.format(msg.ranges[90]))
        print('Range at 60 degress: {}'.format(msg.ranges[60]))
        print('Range at 120 degress: {}'.format(msg.ranges[120]))
        print('Range at 270 degress: {}'.format(msg.ranges[270]))
        print('Range at 300 degress: {}'.format(msg.ranges[300]))
        print('Range at 240 degress: {}'.format(msg.ranges[240]))
        
        
        front = msg.ranges[0]
        front1 = msg.ranges[15]
        front2 = msg.ranges[44]
        front_left = msg.ranges[30]
        front_right1 = msg.ranges[345]
        front_right = msg.ranges[330]
        front_right2 = msg.ranges[314]
        
        
        left = msg.ranges[90]
        left1 = msg.ranges[75]
        left2 = msg.ranges[47]
        left_top = msg.ranges[60]
        left_bottom = msg.ranges[105]
        
        
        right = msg.ranges[270]
        right_top = msg.ranges[300]
        right_top1 = msg.ranges[285]
        right_bottom = msg.ranges[255]
        
        # average values
        front_avg = (front + front_left + front_right)/3
        left_avg = (left + left_top + left_bottom)/3
        right_avg = (right + right_top + right_bottom)/3


        dist = 0.1

        if front > dist and front_left > dist and front_right > dist:
          vel.linear.x=0.5
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = 0

        elif left > dist and left_top > dist and left_bottom > dist:
          vel.linear.x=0
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = 1

        elif right > dist and right_top > dist and right_bottom > dist:
          vel.linear.x=0
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = -1
          
        else:
          vel.linear.x=0
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = 0.2

        pub.publish(vel)

vel = Twist()
rospy.init_node('obstacle_avoidance', anonymous=True)     
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)          
sub = rospy.Subscriber('/scan',LaserScan,callback)    

rospy.spin()

