## About Rae
Rae is an __OpenSource__ based modular end-of-arm tool with integrated __eye-in-hand__ depth camera which enables researchers, AI-enthusiasts and engineers to develop and deploy autonomous applications for robot manipulators. The 6 different module-types helps to solve various modern challenges in Robotics as for example bin-picking, packaging or tool-based automation. For more information about the system please visit our [homepage](#).

## [Table of content](#table-of-content)
- [Package Overview](#package-overview)
- [Getting started](#getting-started)
  - [Software Installation](#software-installation)
    - [Install raepy](#install-raepy)
    - [Install the ROS Packages](#install-the-ros-packages)
  - [Start the servers](#start-the-servers)
  - [Run example](#run-example)
- [Services and Actions](#services-and-actions)
- [Contribution](#contribution)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=false
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

# Package Overview
[Softwarestack,Package overview map]

The `raeros_system` package for ROS is necessary to start servo, rack and radialgripper server. 
It consists of the following files:
* [launch/system.launch](https://github.com/romzn/raeros_system/blob/master/launch/system.launch) - launches the configured module servers
* [scripts/example.py](https://github.com/romzn/raeros_system/blob/master/scripts/example.py) - example to show basic functions
* [launch/example.launch](https://github.com/romzn/raeros_system/blob/master/launch/example.launch) - inclued `system.launch` and starts a node with `scripts/example.py`

# Getting started
> **Get the Hardware:** First of all you need the right Hardware. The [raeware repository](#raeware-repo) helps you to __buy-or-make__ your personal autonomy effector.


## Software Installation
First install `raepy` which is an python based software interface and then install the ROS-packages.

### Install raepy

```bash
pip3 install raepy
```
If you want to modify the software-driver raepy, you have to build the sources in your workspace.
In order to do that just clone the repository, build and install it.

```bash
git clone github.com/romzn/raepy.git
cd raepy

## Build repository and Install
python3 -m pip install --upgrade build
pip3 -m build
pip3 install .
```


### Install the ROS Packages
Choose the modules depending on your hardware configuration. At the moment these modules are available:

* [Vacuum-Module](https://github.com/romzn/raeros_vacmod)
* [Radialgrippers](https://github.com/romzn/raeros_radialgripper)
* [Linear-Rack](https://github.com/romzn/raeros_rack/tree/melodic)
* [Servo](https://github.com/romzn/raeros_servo/tree/melodic)

The following commands let you install all available modules.

```bash
cd ~/catkin_ws/src &&
git clone -b melodic https://github.com/romzn/raeros_vacmod.git &&
git clone -b melodic https://github.com/romzn/raeros_radialgripper.git &&
git clone -b melodic https://github.com/romzn/raeros_rack.git &&
git clone -b melodic https://github.com/romzn/raeros_servo.git &&
cd ../../ &&
catkin_make 
```

## Start the servers
Each installed package includes an server which handle requests from a client. 

Before starting the servers you have to decide which modules shall be enabled.
For this look inside the launch file: `/launch/system.launch` and choose the modules you need by setting the arguments to true.

```xml
<launch>
    <arg name="servo" default="true"/>
    <arg name="rack" default="true"/>
    <arg name="radialgripper" default="true"/>
    <arg name="vacmod" default="true"/>

    <node pkg="rae_servo_server" name="rae_servo_server" type="rae_servo_server.py" output="screen" respawn="false" if="$(arg servo)"/>
    <node pkg="rae_rack_server" name="rae_rack_server" type="rae_rack_server.py" output="screen" respawn="false" if="$(arg rack)"/>
    <node pkg="rae_radgripper_server" name="rae_radgripper_server" type="rae_radgripper_server.py" output="screen" respawn="false" if="$(arg radialgripper)"/>
    <node pkg="rae_vacmod_server" name="rae_vacmod_server" type="rae_vacmod_server.py" output="screen" respawn="true" if="$(arg vacmod)"/>
</launch>

```

Now connect to the RPi on the Rae via `ssh romzn@rae.local` and `raeisgreat` as password.
After successful login launch the system with:

```bash
roslaunch raeros_system system.launch
```
## Run example
The example executes some basic functionalites which is recommended to study.
It is located in [scripts/example.py](https://github.com/romzn/raeros_system/blob/master/scripts/example.py).
To start it execute:

```bash
rosrun raeros_system example.py
```

It leads you through the calibration procedure. And shows vacuum and gripping capabilities.

# Services and Actions
[Overview Image]

# Contribution
Feel free to contribute to the project and pin your issues and ideas.