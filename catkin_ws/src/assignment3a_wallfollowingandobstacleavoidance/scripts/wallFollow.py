#!/usr/bin/env python3

import matplotlib.pyplot as plt
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan #message type used by /scan topic for laser scan data
import math #so I can use pi, cos and sin
import numpy as np

#function that looks at all 
def groupFurthest(ranges):
	#don't assume that INF is always present
	
	#need to find groups of INF and groups of real values
	
	
#fuction to run everytime scan data is recieved
def callback(msg):
	#any range further than the max range of the lidar will get returned as INF.
	#so can't just find the furthest away point (np.argmax(ranges)) since there will be a group of INFs and need to take middle ones

	#IND IS NOT RETURNING FURTHEST DIRECTION!!
	ind = np.argmax(msg.ranges) #returns index of greatest value in np array
	print(ind)
	
	#we want the greatest ind to always be 0 (robot is travling towards a clear path)
	#NEED TO TURN BASED ON HOW OFF FAR FROM 0 ind IS
	#IF IND > 0, POSITIVE TURN
	while ind != 0:
		print("turning")
		print(ind)
		#stop moving and turn until it is
		vel.linear.x = 0.2
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = ind/9
			
		publisher.publish(vel)
			
		rate.sleep()
	#rospy.loginfo(type(msg.ranges))
	#rospy.loginfo(max(msg.ranges))
	

if __name__ == '__main__':
	try:
		#can only call init_node once in a python script! (launch file only created one node)
		rospy.init_node('turtlesim_controller',anonymous=True)
		#our one node will both subscribe to /scan and publish to /cmd_vel
		
		#publisher:
		publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		vel = Twist() #create Twist message variable to write velocity in and publish
		rate = rospy.Rate(10)
		
		#subscriber:
		subscriber = rospy.Subscriber("/scan", LaserScan, callback)
		#rospy.spin()

		while not rospy.is_shutdown():
			print("straight")
			vel.linear.x = 0.2
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			vel.angular.z = 0
			
			publisher.publish(vel)
			
			rate.sleep()
		
	except rospy.ROSInterruptException:
		pass
