#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


if __name__ == '__main__':
	try:
		
		#launch file created node that opened python file. Still need node to control turtlebot
		rospy.init_node("whatever",anonymous=True)
		#to move the turtle in a circle we need to change it's linear and angular velocity. We do this by publishing to the /cmd_vel topic. So need to create a publisher:
		publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		
		vel = Twist() #move forward at a velocity of 1 and rotate at 0.5 rad/s
		rate = rospy.Rate(10)

		while not rospy.is_shutdown():
			#slow settings:
			vel.linear.x = 0.1
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			vel.angular.z = 2
			
			publisher.publish(vel)
			
			rate.sleep()
		
	except rospy.ROSInterruptException:
		pass
