cmake_minimum_required(VERSION 2.8.3)

project(Ball_robot)

find_package(catkin REQUIRED
  roscpp
  rospy
  trajectory_msgs
  std_msgs
  gazebo_ros
  controller_manager
  joint_state_controller
  position_controllers
  controller_interface
  robot_state_publisher
)

catkin_package(CATKIN_DEPENDS  roscpp rospy trajectory_msgs std_msgs gazebo_ros controller_manager joint_state_controller position_controllers controller_interface robot_state_publisher)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
