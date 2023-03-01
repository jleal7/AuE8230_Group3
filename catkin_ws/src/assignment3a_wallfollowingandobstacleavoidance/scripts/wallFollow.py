#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan #message type used by /scan topic for laser scan data

#fuction to run everytime scan data is recieved
def callback(msg):
	print("1")

if __name__ == '__main__':
	try:
		rospy.init_node('turtlesim_controller',anonymous=True) #can only call init_node once in a python script! launch file only created one node
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
			vel.linear.x = 1
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			vel.angular.z = 0
			
			publisher.publish(vel)
			
			rate.sleep()
		
	except rospy.ROSInterruptException:
		pass
