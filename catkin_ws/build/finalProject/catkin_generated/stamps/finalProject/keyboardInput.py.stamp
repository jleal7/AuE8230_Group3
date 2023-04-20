#!/usr/bin/env python3

import keyboard
import matplotlib.pyplot as plt
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan #message type used by /scan topic for laser scan data
import math #so I can use pi, cos and sin
import numpy as np
	
if __name__ == '__main__':
	try:
		rospy.init_node('turtlesim_controller',anonymous=True)
		
		#publisher:
		publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		vel = Twist() #intialize vel as a Twist message
		rate = rospy.Rate(10)
		
		#subscriber:
		subscriber = rospy.Subscriber("/scan", LaserScan, callback)

		#code won't run unless this while loop is present so have it with a pass
		while not rospy.is_shutdown():
			pass
		
	except rospy.ROSInterruptException:
		pass
