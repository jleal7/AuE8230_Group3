# Wall Follow

## Execute Launch File

roslaunch assignment3a_wallfollowingandobstacleavoidance wallFollow.launch --screen


## Launch File Explanation

Launch file consists of 5 sections:

1. Set initial x,y,z position of turtlebot in world
2. Find the world we want to launch in gazebo (we saved the provided world files in /worlds folder)
3. Load xacro file for turtlebot3 burger
4. Launch first node which is gazebo simulator with our chosen world
5. Launch second node which is the python script to control the turtlebot

NOTE: Odd that gazebo calculated a different trajectory for the turtlebot when screen was being recorded vs not.

# Part 2 - Obstacle Avoidance

For this the scan data from the Lidar has to be used to sense the obstacles and take evasive maneuvers to avoid it.
The 1st part includes the logic which is taken from the hint in the question itself, but instead of segregating the zones into multiple angle instances and taking the average and comparing them to the the orientation, the zones were converted into segments of 4-6 and each segment value was used individually to obtain the obstacles nearby and rotate based on the fixed distance or safe distance, which was set as 0.5
If the front distance > 0.5 then the bot can continue straight, the same applies for left and right. 
This process continues as the bot traverses around the entire map.
