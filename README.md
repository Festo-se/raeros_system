# About
The __raeros_system__ package for ROS is necessary to start servo, rack and radialgripper server

# Installation
First install `raepy` which is an python based software interface and then install the ROS-packages which has raepy as dependency
## Install raepy dependency
If you want to modify the software-drive raepy, you have to build the sources in your workspace.
In order to do that just clone the repository, build and install it.

```bash
git clone github.com/romzn/raepy.git
cd raepy

## Build repository and Install
python3 -m pip install --upgrade build
pip3 -m build
pip3 install .
```
otherwise just install the package via pip
```bash
pip3 install raepy
```

## Install the ROS Packages
Install the packages from the modules you need. 
At the moment these modules are available:

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

## Start the Servers
Each installed package includes an server which handle requests from a client. 
These Servers should be started in the *RPI* on the Rae.

Before starting you have to decide which modules shall be enabled
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

Now connect to the Rae via `ssh romzn@rae.local` and `raeisgreat` as password.
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

# Contribution
Feel free to contribute to the project and pin your issues.
