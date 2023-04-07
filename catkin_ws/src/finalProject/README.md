# Part 1 - Wall Follow

## Gazebo Simulation

### Execute Launch File

roslaunch finalProject simulation.launch --screen

### Launch File Explanation


## Real Life

## Launch file explenation

Launch file just creates a node which calls the WallFollow.py script.

## Script Explanation

1. Erase back half of ranges to avoid two possible solutions.

2. GOAL: head for the furthest away point.

3. 2 possible cases: 1. Furthest point is within max range of lidar so it is a singular value. 2. Furthest point is outside max range of lidar so it is inf, could be group of infs.

4. Case 1: turn until furthest away point is at center of robot.

5. Case 2: detect group of infs and take average value. Turn until that angle is at center of robot.

6. Safety net that makes robot stop moving and turn away from wall if it ever gets too close.

### Execute Launch File

1. run roscore on laptop

2. roslaunch turtlebot3_bringup turtlebot3_robot.launch on turtlebot

3. roslaunch finalProject realLife.launch --screen
