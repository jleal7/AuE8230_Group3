# Part 1 - Wall Follow

## Gazebo Simulation

### Execute Launch File


### Launch File Explanation


## Real Life

### Execute Launch File

1. run roscore on laptop

2. roslaunch turtlebot3_bringup turtlebot3_robot.launch on turtlebot

3. roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch on turtlebot

4. roslaunch finalProject wallFollow.launch --screen

### Launch File Explanation

The launch file for the real life implementation is the same as for the gazebo implementation but does not need to call Gazebo and calls LineTrack_real.py instead of LineTrack_gazebo.py. The only change in LineTrack_real.py versus LineTrack_gazebo.py was that our track was white and not yellow. So we took a screenshot of the image and used a color picker to tune in our new track color values. The linear and angular speeds were also cut in half to make sure track of line was not lost.
