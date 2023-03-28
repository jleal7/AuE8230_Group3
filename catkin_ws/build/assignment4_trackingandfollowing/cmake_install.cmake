# Install script for directory: /home/jairo/Desktop/AuE8230_Group3/catkin_ws/src/assignment4_trackingandfollowing

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/assignment4_trackingandfollowing.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/assignment4_trackingandfollowing/cmake" TYPE FILE FILES
    "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/assignment4_trackingandfollowingConfig.cmake"
    "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/assignment4_trackingandfollowingConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/assignment4_trackingandfollowing" TYPE FILE FILES "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/src/assignment4_trackingandfollowing/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/assignment4_trackingandfollowing" TYPE PROGRAM FILES "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/LineTrack_gazebo.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/assignment4_trackingandfollowing" TYPE PROGRAM FILES "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/follow_line_step_hsv.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/assignment4_trackingandfollowing" TYPE PROGRAM FILES "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/line_follower_basics.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/assignment4_trackingandfollowing" TYPE PROGRAM FILES "/home/jairo/Desktop/AuE8230_Group3/catkin_ws/build/assignment4_trackingandfollowing/catkin_generated/installspace/move_robot.py")
endif()

