# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/darknet_ros_msgs;/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/assignment4_trackingandfollowing;/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/cv_bridge;/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/aue_finals;/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/assignment3a_wallfollowingandobstacleavoidance;/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/assignment2B_turtlebotteleop;/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/assignment1c_turtlebot3;/home/jairo/Desktop/AuE8230Spring23_JairoLeal/catkin_ws/devel;/home/jairo/catkin_ws/devel;/home/jairo/Desktop/Autonomy/ROS_workspace/devel;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/jairo/Desktop/AuE8230_Group3/catkin_ws/devel_isolated/darknet_ros/env.sh')

output_filename = '/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build_isolated/darknet_ros/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
