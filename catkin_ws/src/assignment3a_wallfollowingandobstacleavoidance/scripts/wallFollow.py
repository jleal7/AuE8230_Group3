#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan #message type used by /scan topic for laser scan data
import matplotlib.pyplot as plt
import math #so I can use pi, cos and sin

fig = plt.figure()
ax = fig.add_subplot(projection='polar')
ax.set_rmax(10)
ax.grid(True)
plt.show(block=False)

#fuction to run everytime scan data is recieved
def callback(msg):
	plt.cla()

	#convert polar coordinates r and theta to x and y so can plot with matplotlib
	#for ind,value in enumerate(msg.ranges):
	#	theta = ind * (math.pi/180); #index is angle in degrees, need to convert to rad
	#	x = value*math.cos(theta) #r is value (value inside current index of ranges)
	#	y = value*math.sin(theta)
	#	plt.scatter(x,y)
	#	#plt.scatter(theta,value)
	
	ax.scatter(range(0,360), msg.ranges)
		
	plt.show(block=False)
	plt.pause(.1)

if __name__ == '__main__':
	try:		
		#can only call init_node once in a python script! launch file only created one
		rospy.init_node('turtlesim_controller',anonymous=True)
		#our one node will both subscribe to /scan and publish to /cmd_vel
		
		#publisher:
		publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		
		vel = Twist() #move forward at a velocity of 1 and rotate at 0.5 rad/s
		rate = rospy.Rate(10)
		
		#subscriber:
		subscriber = rospy.Subscriber("/scan", LaserScan, callback)
		#rospy.spin()

		while not rospy.is_shutdown():
			#slow settings:
			vel.linear.x = .2
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			vel.angular.z = 0
			
			publisher.publish(vel)
			
			rate.sleep()
		
	except rospy.ROSInterruptException:
		pass
