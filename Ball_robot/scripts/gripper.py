#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Float64
from controller_manager_msgs.srv import SwitchController

def move_gripper(lh_position, rh_position):
    rospy.init_node('gripper_control', anonymous=True)
    pub = rospy.Publisher('/hand_controller/command', JointTrajectory, queue_size=10)

    # Wait for the publisher to be ready
    rospy.sleep(1)

    # Create a JointTrajectory message
    traj = JointTrajectory()
    traj.joint_names = ['LH_joint', 'RH_joint']

    point = JointTrajectoryPoint()
    point.positions = [lh_position, rh_position]
    point.time_from_start = rospy.Duration(1.0)
    traj.points = [point]

    pub.publish(traj)
    rospy.loginfo(f"Gripper moved to positions LH: {lh_position}, RH: {rh_position}")

if __name__ == "__main__":
    try:
        
        move_gripper(3.14, 3.14)  # Open the gripper
        rospy.sleep(2)
        move_gripper(0.0, 0.0)    # Close the gripper
    except rospy.ROSInterruptException:
        rospy.logerr("ROS node interrupted!")
    except rospy.ROSException as e:
        rospy.logerr(f"Error: {e}")
