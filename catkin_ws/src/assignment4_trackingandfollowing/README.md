# Part 1 - Line Tracking

## Gazebo Simulation

### Execute Launch File

roslaunch assignment4_trackingandfollowing laneTrack_gazebo.launch --screen

### Launch File Explanation

The launch file contains two sections. The first section is a copy paste of the default launching gazebo simulation. Two changes were made to this section:

1. The world was changed to the TA-provided world with the yellow line to track.

2. The starting position was set to be on the yellow line but not tangent to it. The robot starts 90 deg to the the line so it cannot see the line. This made us have to implement an algorithm was was able to be robust enough to loose the line and find it again. We thought it was fine to place the robot on the line since in real life we will also start the robot on the line.

The second section calls the LineTrack_gazebo.py python script. This script contains 3 main sections:

1. MoveTurtlebot3 class definition. This was a copy paste from the move_robot.py script provided by the TAs. The original implementaton used "from move_robot import MoveTurtlebot3" but an import error kept occuring that could not be solved. To avoid this issue the whole MoveTurtlebot3 class was just copy pasted into the LineTrack_gazebo.py file.

2. LineFollower class definition which was provided by the TAs.

3. Main section which was provided by the TAs.

The trace callback of the program is as follows:

1. All the required packaged are imported.

2. rospy.init_node is called outside of any function and right after the imports because you can't do anything with the bot until you have initialized the node.

3. twist_object and moveTurtlebot3_object are initialized outside all function since they are called by many functions so need global scope. The MoveTurtlebot3's constructor creates both a publisher and subscirber to the /cmd_vel topic but the callback on the subscriber is only used to save the topic for error checking purposes. It also sets the publishing rate to the motors at 40 Hz.

4. "if __name__ == '__main__':" is finally called as the first function to start the program and it simply calls the main function.

5. main makes the robot start spinning by default if it does not detect the line. It also sets the rate to read from the LIDAR to 40 Hz. This was found to be a good compromise of having double send message errors and minimizing oscillation of the robot. Lastly, it creates a LineFollower object whose constructor starts a CV bridge and creates a subscriber node to the camera topic. The subscriber node's callback does all the heavy lifting. It crops the bottom of the image, detects the yellow of the track and compares the blob of the yellow track to the center of the image. If the blob if to the left of center steer left and vice-versa. The foundLine boolean was used for the robot to know if it should stop and spin till it finds a line or keep tracking the blob. You could keep moving if you loose the line for a little bit assuming you were going in the right direction but to be safe our robot stops and turns.

## Real Life

### Execute Launch File

1. run roscore on laptop

2. roslaunch turtlebot3_bringup turtlebot3_robot.launch on turtlebot

3. roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch on turtlebot

4. roslaunch assignment4_trackingandfollowing laneTrack_real.launch --screen

### Launch File Explanation

The launch file for the real life implementation is the same as for the gazebo implementation but does not need to call Gazebo and calls LineTrack_real.py instead of LineTrack_gazebo.py. The only change in LineTrack_real.py versus LineTrack_gazebo.py was that our track was white and not yellow. So we took a screenshot of the image and used a color picker to tune in our new track color values. The linear and angular speeds were also cut in half to make sure track of line was not lost.
