#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


#class obstacleAvoidance():
#def __init__(self):
        
#initializing the node
  

def callback(msg):
        
        #print('front 0 deg: {}'.format(msg.ranges[0]))
        #print('front_left 30 deg: {}'.format(msg.ranges[30]))
        #print('front_right 330 deg: {}'.format(msg.ranges[330]))
        #print('left 90 deg: {}'.format(msg.ranges[90]))
        #print('left_top 60 deg: {}'.format(msg.ranges[60]))
        #print('left_bottom 105 deg: {}'.format(msg.ranges[105]))
        #print('right 270 degress: {}'.format(msg.ranges[270]))
        #print('right_top 90 deg: {}'.format(msg.ranges[300]))
        #print('right_bottom 90 deg: {}'.format(msg.ranges[255]))
        

        

           
        
        front = msg.ranges[0]
        #front1 = msg.ranges[15]
        #front2 = msg.ranges[44]
        front_left = msg.ranges[30]
        #front_right1 = msg.ranges[345]
        front_right = msg.ranges[330]
        #front_right2 = msg.ranges[314]
        
        
        left = msg.ranges[90]
        #left1 = msg.ranges[75]
        #left2 = msg.ranges[47]
        left_top = msg.ranges[60]
        left_bottom = msg.ranges[105]
        
        
        right = msg.ranges[270]
        right_top = msg.ranges[300]
        #right_top1 = msg.ranges[285]
        right_bottom = msg.ranges[255]
       
        
        #front
        if front==0:
           front = 20
        else:
           front=front
        
        if front_left==0:
           front_left = 20
        else: 
           front_left=front_left

        if front_right==0:
           front_right = 20
        else: 
           front_right=front_right
        #left
        if left==0:
           left = 20
        else: 
           left=left
        if left_top==0:
           left_top = 20
        else: 
           left_top=left_top
        if left_bottom==0:
           left_bottom = 20
        else: 
           left_bottom=left_bottom
        #right
        if right==0:
           right = 20
        else: 
           right=right
        if right_top==0:
           right_top = 20
        else: 
           right_top=right_top
        if right_bottom==0:
           right_bottom = 20
        else: 
           right_bottom=right_bottom

        print('front 0 deg: {}'.format(front))
        print('front_left 30 deg: {}'.format(front_left))
        print('front_right 330 deg: {}'.format(front_right))
        print('left 90 deg: {}'.format(left))
        print('left_top 60 deg: {}'.format(left_top))
        print('left_bottom 105 deg: {}'.format(left_bottom))
        print('right 270 degress: {}'.format(right))
        print('right_top 90 deg: {}'.format(right_top))
        print('right_bottom 90 deg: {}'.format(right_bottom))
        
        
        
        # average values
        front_avg = (front + front_left + front_right)/3
        left_avg = (left + left_top + left_bottom)/3
        right_avg = (right + right_top + right_bottom)/3


        dist = 0.5
        if front > dist and front_left > dist and front_right > dist:
          vel.linear.x=0.05
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = 0

        elif left > dist and left_top > dist and left_bottom > dist:
          vel.linear.x=0.05
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = 1

        elif right > dist and right_top > dist and right_bottom > dist:
          vel.linear.x=0.05
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = -1
          
        else:
          vel.linear.x=0.08
          vel.linear.y=0
          vel.linear.z=0

          vel.angular.x = 0
          vel.angular.y = 0
          vel.angular.z = 0
        pub.publish(vel)

vel = Twist()
rospy.init_node('obstacle_avoidance', anonymous=True)     
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)          
sub = rospy.Subscriber('/scan',LaserScan,callback)    

rospy.spin()

