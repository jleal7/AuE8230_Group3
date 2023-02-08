#!/usr/bin/env python3

import roslaunch
import rospy
#from echoing gazebo, it uses the same Twist geometry_msgs as turtlesim
from geometry_msgs.msg import Twist #needed to send velocity messages to /turtle1/cmd_vel topic

#need to use try and except structure so I can use ^C in terminal to quit
if __name__ == '__main__':
	try:
		#1. Launch empty world with turtlebot3 in Gazebo using provided launch file
		rospy.init_node('turtlebot_controller', anonymous=True)
		uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
		roslaunch.configure_logging(uuid)
		launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/jairo/Desktop/AuE8230_Group3/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/launch/turtlebot3_empty_world.launch"])
		launch.start()
		rospy.loginfo("started")
		
		#2. Move turtlebot in a circle
		#rospy.init_node('turtlesim_controller',anonymous=True)
		#to move the turtle in a circle we need to change it's linear and angular velocity. We do this by publishing to the /cmd_vel topic. So need to create a publisher:
		publisher = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		#ROS makes us define a node. Even though I initialized a publisher, gotta make it a node
		
		vel = Twist() #move forward at a velocity of 1 and rotate at 0.5 rad/s
		rate = rospy.Rate(10)
		#tried without loop since we only need to send command once to go in a circle but would not work. Node would not even initialize without loop even though I ran init_node
		while not rospy.is_shutdown():
			#slow settings:
			#vel.linear.x = 0.1
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			#vel.angular.z = 0.1
			
			#medium settings:
			#vel.linear.x = 0.3
			#vel.angular.z = 0.3
			
			#fast settings:
			vel.linear.x = 1
			vel.angular.z = 1
			
			publisher.publish(vel)
			
			rate.sleep()
		
	except rospy.ROSInterruptException:
		print("FAILED: inside exception loop")
		process.stop()
		pass
