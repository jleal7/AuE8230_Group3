# Real Life

## Bringup Commands

1. LAPTOP: run roscore

2. TURTLEBOT: roslaunch turtlebot3_bringup turtlebot3_robot.launch

3. TURTLEBOT: roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch

4. LAPTOP: roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch

4. LAPTOP: roslaunch apriltag_ros continuous_detection.launch

5. rqt

6. LAPTOP: roslaunch darknet_ros darknet_ros.launch (close before stage 4!)

7. LAPTOP: roslaunch finalProject realLife.launch --screen







# Simulation

## Bringup Commands

1. roslaunch darknet_ros darknet_ros_gazebo.launch (close before stage 4!) 

2. roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration_gazebo.launch

3. roslaunch apriltag_ros continuous_detection_gazebo.launch

4. rqt

5. roslaunch finalProject simulation.launch --screen

### Launch File Explanation

## Wall Follow Code Explanation

1. Erase back half of ranges to avoid two possible solutions.

2. GOAL: head for the furthest away point.

3. 2 possible cases: 1. Furthest point is within max range of lidar so it is a singular value. 2. Furthest point is outside max range of lidar so it is inf, could be group of infs.

4. Case 1: turn until furthest away point is at center of robot.

5. Case 2: detect group of infs and take average value. Turn until that angle is at center of robot.

6. Safety net that makes robot stop moving and turn away from wall if it ever gets too close.
