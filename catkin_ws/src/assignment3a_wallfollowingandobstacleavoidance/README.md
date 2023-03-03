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
