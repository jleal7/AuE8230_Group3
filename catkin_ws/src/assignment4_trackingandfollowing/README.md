# Part 1 - Line Tracking

## Gazebo Simulation

### Execute Launch File

roslaunch assignment4_trackingandfollowing laneTrack_gazebo.launch --screen

### Launch File Explanation

The launch file contains two sections. The first section is the default copy-paste of launching the gazebo simulation. Two changes were made to this section:

1. The world was changed to the TA-provided world with the yellow line to track.

2. The starting position was set to be on the yellow line but not tangent to it. Initially the robot is at 90 deg to the the line so it cannot see the line from its camera. This made us have to implement an algorithm was was able to be robust enough to loose the line and find it again. We thought it was fine to place the robot on the line since in real life we will also start the robot on the line.

The second section calls the follow_line_step_hsv_me.py python script. This script contains 3 sections:

1. MoveTurtlebot3 class definition. This was a copy paste from the move_robot.py script provided by the TAs. The original implementaton used "from move_robot import MoveTurtlebot3" but an import error kept occuring and could not be solved. To avoid this issue the whole class was just copy pasted into the follow_line_step_hsv_me.py file.

2. LineFollower class definition which was provided by the TAs.

3. Main section which was provided by the TAs.

The trace callback of the program is as follows:

1. All the required packaged are imported.

2. rospy.init_node is called outside of any function and right after the imports because you can't do anything with the bot until you have initialized the node.

3. twist_object and moveTurtlebot3_object are initialized outside any function since they are called by many functions so need global scope.

4. "if __name__ == '__main__':" is finally called as the first function to start the program and it simply calls the 

The biggest challenges were first making the robot stop oscillating around the center of the track even while stationary. Fixed by rasing rate of polling from lidar. Two was the robot knowing if it had found a line or not. So used foundLine boolean...

## Real Life
