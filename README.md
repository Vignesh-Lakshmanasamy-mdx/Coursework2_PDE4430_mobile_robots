# Coursework2_PDE4430_mobile_robots

**Coursework task** :

 -- To create a own robot which can carry the 3 different size balls to the pen or goal post.

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

**Step 5 ** :

-- Design the front shutter for the robot to lock the ball in place.

**Step 6** :

-- Assemble the entire robot in the soldiworks. Two wheels at the back of the robot and two caster wheel at the front area and the locking door or end effector in the pin in have

