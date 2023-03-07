# Part 1 - Wall Follow

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

Steps to launch:
1. As all the parameters are preset, and it is a standalone code, just the Launch file has to be run.
2. Rosrun 

# Part 3 - Obstacle Avoidance - Actual Turtlebot

Setup - As instructed we setup a few obstacles on the 4th floor CGEC for the actual run of the obstacle avoidance. 
The wander.py file was run.
Issues: Unlike gazebo /scan where the lidar returned inf value when it exceeded a certain threshold, the actual Lidar returned a value of 0. Which meant that when ever the front reading returned 0, the bot stopped as according to the code if the value went below the threshold, it should stop. 
A find function was implemented to parse the 0 values and set it to some set value = 20, but that also did not seem to work.
This can be seen in the videos uploaded to the videos folder (4 runs uploaded)

# Part 4 - Emergency Braking

For this task, it uses a similar logic as the obstacle avoidance part, hence with a slight change to the code, the emergency braking maneuver could be performed.
The set limit or threshold was set and the vel.linear.x was set to 0 as the deitance or /scan data went below the threshold (dist).
