# Mobile Inverted Pendulum ROS Package

Hi! I'm your first Markdown file in **StackEdit**. If you want to learn about StackEdit, you can read me. If you want to play with Markdown, you can edit me. Once you have finished with me, you can create new files by opening the **file explorer** on the left corner of the navigation bar.
Gazebo Simulation of mobile inverted pendulum.

## Instructions

In order to run this package, add it to your catkin workspace. You can use the following commands:
If you don't have a catkin workspace initialized:

```
mkdir -p ~/catkin_ws/src
cd catkin_ws/src/
```

Clone this repo.

```
cd ~/catkin_ws/
catkin_make
```

Now source your workspace from the catkin base directory and continue:

`source devel/setup.bash`

or add to ~/.bashrc

`echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`

Start roscore: `roscore`

### Open a New Terminal Window

Gazebo Simulation: `roslaunch controls inverted_pendulum_sim.launch`

