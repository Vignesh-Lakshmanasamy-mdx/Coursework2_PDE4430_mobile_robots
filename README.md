# Coursework2_PDE4430_mobile_robots

**Coursework task** :

 -- To create a own robot which can carry the 3 different size balls to the pen or goal post.

**Process involved** :

**Step 1**:

-- Designing our own robot in Solidworkd or Fusion 360 or Freecad. 
-- I am using solidworks 2025 to create my design
-- Install the URDF pulgin for the software to convert the design to urdf file.

**Step2**:

-- create the base part of the robot as "base_link"

![Screenshot 2025-01-15 232500](https://github.com/user-attachments/assets/1aefeaa2-f5a7-4078-b3b9-3ebad79c7696)

-- the base size is 400 x 400 mm and 30 mm extruded shaft for the wheel connection.

-- the cutout to hold the ball is 350 x 350 mm. 

**Step 3** :

-- create the wheel part file for the robot as "RL and RR" (Rear Left and Rear Right)

![Screenshot 2025-01-15 233537](https://github.com/user-attachments/assets/0071827d-1f23-4e33-aa7c-0fccb7e4cf4a)

-- the wheel diameter is 100 mm and wheel to wheel distance is 420 mm, both this parameters are need in gazebo pulgin for differential drive.

**Step 4** :

-- design the Caster wheel for the robot
-- the caster wheel should touch the base reference plane of the robot design. if not it may cause balancing problem in the robot in gazebo environment

**Step 5** :

-- Design the front shutter for the robot to lock the ball in place.

**Step 6** :

-- Assemble the entire robot in the soldiworks. Two wheels at the back of the robot and two caster wheel at the front area and the locking door or end effector in the pin in have

**Step 7** :

-- create axis, co ordinate system and point for each wheel,caster and end effector.

![Screenshot 2025-01-15 235249](https://github.com/user-attachments/assets/c4eec451-babb-41f4-bb58-e763491baafb)

-- as shown in the image. name it in a proper way to identify in easily.

-- create the plane and co ordinate for the base plane level, this should be the gazebo ground after the convertion to urdf.

**Step 8** :

![Screenshot 2025-01-15 235643](https://github.com/user-attachments/assets/1debf41f-bb4f-486c-9a72-cf89804b8a5f)

-- as shown in the figure create the parent and child link for the robot with appropriate axis and coordinates

-- for the joint type : wheel and caster is continuous but the end effector is revolute joints

**Step 9** :

-- go to Preview and Export -> clearly check the axis , coordinates, joint type and max limit for the components

-- click next to check the inertia and weight of the robot to avoid gazebo conflicts. 

![Screenshot 2025-01-16 000231](https://github.com/user-attachments/assets/16053c35-b237-428d-b3cc-d2b85ff3c7df)

**Step 10** :

-- export the file . solidworks automatically generate the urdf,mesh,config,package,cmake_list and launch files.

-- copy the file and bring to Catkin_WS /src file 

--  Edit the urdf file to add the foot_print for the robot.

-- add the gazebo plugin for the differential drive
https://classic.gazebosim.org/tutorials?tut=ros_gzplugins#DifferentialDrive

**Instruction to execute the project** :

1. Pull the file from github and add it to the catkin_ws/src folder
2. In terminal go to catkin_ws and run

          catkin_make
          source devel/setup.bash

3. To get entire assessment world, robot and the ball in gazebo type in new terminal, 

          roslaunch Ball_robot coursework.launch

![Screenshot 2025-01-16 002837](https://github.com/user-attachments/assets/7a998e38-589d-4659-a16b-afe320c62c09)

5. To run the robot using teleoperation keyboard, use

          rosrun teleop_twist_keyboard teleop_twist_keyboard.py

   if teleop_twist_keyboard not installed follow the instruction in the http://wiki.ros.org/teleop_twist_keyboard

6. To run the custom made teleop keyboard, use

          rosrun Ball_robot keyboard.py

7. To view the rqt_graph

         rosrun rqt_graph rqt_graph
   
![Screenshot 2025-01-16 003006](https://github.com/user-attachments/assets/c696f26a-10c5-4995-a9c8-146759f30f78)

