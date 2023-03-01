#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan #message type used by /scan topic for laser scan data

#fuction to run everytime scan data is recieved
def callback(msg):
	#print(msg.ranges[0:72])
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
	pass

if __name__ == '__main__':
	try:
		#going to need a publisher to tell turtlebot how to move and subscriber to get scan data
		
		#publisher:
		rospy.init_node('turtlesim_controller',anonymous=True)
		publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		
		vel = Twist() #move forward at a velocity of 1 and rotate at 0.5 rad/s
		rate = rospy.Rate(10)
		
		#subscriber:
		rospy.init_node('scan_values', anonymous=True)
		subscriber = rospy.Subscriber("/scan", LaserScan, callback)
		rospy.spin()

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
