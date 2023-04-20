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
		
		while True:
			if keyboard.read_key() == 'a':
				print(a)

		#code won't run unless this while loop is present so have it with a pass
		while not rospy.is_shutdown():
			pass
		
	except rospy.ROSInterruptException:
		pass
