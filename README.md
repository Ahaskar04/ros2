# ROS2 Quick Reference Guide

A comprehensive reference for common ROS2 commands and concepts.

---

## Table of Contents

- [Package Management](#package-management)
- [Building Packages](#building-packages)
- [Running Nodes](#running-nodes)
- [Visualization Tools](#visualization-tools)
- [Turtlesim Demo](#turtlesim-demo)
- [Topics](#topics)
- [Recording & Playback (rosbag)](#recording--playback-rosbag)
- [Services](#services)
- [Interfaces](#interfaces)
- [Parameters](#parameters)
- [Launch Files](#launch-files)

---

## Package Management

Create a new ROS2 package:

```bash
ros2 pkg create package_name
```

---

## Building Packages

Build a specific package (run from your `ros2_ws` directory):

```bash
colcon build --packages-select my_py_pkg
```

Source your environment after building:

```bash
source ~/.bashrc
```

> **Note:** After creating a node and building with `colcon build`, ROS doesn't automatically know about your new package. Sourcing "refreshes" your terminal—you can also just restart your terminal.

### Build Options

| Command | Description |
|---------|-------------|
| `colcon build --packages-select my_py_pkg` | Normal build. Copies Python files to `install/` folder. Must rebuild after every code change. |
| `colcon build --packages-select my_py_pkg --symlink-install` | Symlink build. Creates symbolic links to source files. Changes apply immediately without rebuilding. Files must be executable (`chmod +x`). |

---

## Running Nodes

Run a node (package name followed by executable name):

```bash
ros2 run my_py_pkg py_node
```

List all running nodes:

```bash
ros2 node list
```

Run a node with a custom name (allows multiple instances):

```bash
ros2 run my_py_pkg py_node --ros-args -r __node:=abc
```

---

## Visualization Tools

Launch ROS2 GUI tools:

```bash
rqt
rqt_graph
```

---

## Turtlesim Demo

Launch the turtlesim window:

```bash
ros2 run turtlesim turtlesim_node
```

Control the turtle with keyboard:

```bash
ros2 run turtlesim turtle_teleop_key
```

---

## Topics

A **topic** is a named bus over which nodes exchange messages.

### Key Characteristics

- Unidirectional data stream (publisher/subscriber model)
- Anonymous communication
- Each topic has a specific message type
- A node can have many publishers/subscribers for different topics

> *Think of it like a radio station: publishers broadcast, subscribers tune in.*

### Topic Commands

List all active topics:

```bash
ros2 topic list
```

Subscribe to a topic and print messages:

```bash
ros2 topic echo /robot_news
```

Get topic info (type, publisher/subscriber count):

```bash
ros2 topic info /robot_news
```

**Example output:**

```
Type: example_interfaces/msg/String
Publisher count: 1
Subscription count: 0
```

Show message type definition:

```bash
ros2 interface show example_interfaces/msg/String
```

Check publishing frequency:

```bash
ros2 topic hz /robot_news
```

Check bandwidth usage:

```bash
ros2 topic bw /robot_news
```

### Remapping Topics

Remap both node name and topic name:

```bash
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=abc
```

> **Important:** If you remap a publisher's topic, you must also remap the subscriber to match!

---

## Recording & Playback (rosbag)

Record data from a topic:

```bash
ros2 bag record /topic_name
```

Get info about a recording:

```bash
ros2 bag info test
```

Replay and publish all recorded data:

```bash
ros2 bag play test
```

Record multiple topics with a custom name:

```bash
ros2 bag record -o test2 /topic1 /topic2
```

Record all topics:

```bash
ros2 bag record -o test3 -a
```

---

## Services

A ROS2 service is a client/server system.

### Key Characteristics

- Supports both synchronous and asynchronous communication
- One message type for request, one message type for response
- A service server can only exist once but can have many clients
- A service is defined by its name and interface

### Example Interface

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```

**Output:**

```
int64 a
int64 b
---
int64 sum
```

### Service Commands

Call a service (test a server through terminal):

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 3, b: 7}"
```

List all services:

```bash
ros2 service list
```

Get service type:

```bash
ros2 service type /service_name
```

Rename a service:

```bash
ros2 run my_py_pkg file_name --ros-args -r old_server_name:=new_server_name
```

> **Note:** If you rename a server's service name, you also need to rename it on the client side.

---

## Interfaces

Interfaces are built on basic primitive data types.

### Useful Resources

- [Example Interfaces](https://github.com/ros2/example_interfaces)
- [Common Interfaces](https://github.com/ros2/common_interfaces) — the `sensor_msgs` interface is particularly helpful

### Interface Commands

Create a custom interfaces package:

```bash
ros2 pkg create my_robot_interfaces
```

List all sourced interfaces:

```bash
ros2 interface list
```

List interfaces for a specific package:

```bash
ros2 interface package my_robot_interfaces
```

---

## Parameters

Set parameters when running a node:

```bash
ros2 run my_py_pkg number --ros-args -p number:=3 -p timer_period:=0.5
```

List all parameters of all nodes:

```bash
ros2 param list
```

Get the default value of a parameter:

```bash
ros2 param get /node_name /param_name
```

Load parameters from a YAML file:

```bash
ros2 run my_py_pkg number --ros-args --param-file ~/path_to_your_params_file.yaml
```

---

## Launch Files

Launch files allow you to start all nodes from a single file.

### Best Practice

Create a dedicated bringup package for launch files:

```bash
ros2 pkg create package_name_bringup
```

Run a launch file:

```bash
ros2 launch my_robot_bringup number_app.launch.xml
```

### XML Launch File Examples

**Rename a node:**

```xml
<launch>
    <node pkg="my_py_pkg" exec="number" name="my_number_publisher"/>
</launch>
```

**Remap a topic:**

```xml
<launch>
    <node pkg="my_py_pkg" exec="number">
        <remap from="/number" to="/my_number"/>
    </node>
</launch>
```

### Namespaces

Add a namespace prefix via command line:

```bash
ros2 run my_py_pkg exec_name --ros-args -r __ns:=/test
```

---

## Quick Command Reference

| Category | Command | Description |
|----------|---------|-------------|
| **Packages** | `ros2 pkg create <name>` | Create new package |
| **Building** | `colcon build --packages-select <pkg>` | Build specific package |
| **Nodes** | `ros2 run <pkg> <exec>` | Run a node |
| **Nodes** | `ros2 node list` | List running nodes |
| **Topics** | `ros2 topic list` | List active topics |
| **Topics** | `ros2 topic echo <topic>` | Print topic messages |
| **Topics** | `ros2 topic info <topic>` | Get topic information |
| **Services** | `ros2 service list` | List all services |
| **Services** | `ros2 service call <srv> <type> <args>` | Call a service |
| **Params** | `ros2 param list` | List all parameters |
| **Params** | `ros2 param get <node> <param>` | Get parameter value |
| **Bag** | `ros2 bag record <topic>` | Record topic data |
| **Bag** | `ros2 bag play <name>` | Replay recorded data |
| **Launch** | `ros2 launch <pkg> <file>` | Run launch file |



<!-- ros2 launch urdf_tutorial display.launch.py model:=/home/ahaskar/my_robot.urdf -->
<!-- TF is the system that tells the robot where things are relative to each other, at all times. -->
<!-- go through the urdf xml page documentation well, includes the different types as well-->
<!-- robot_state_publisher: alreasdy existsing node in ROS, which takes urdf as input and connects to /tf -->
<!-- robot_state_publisher also takes joint_states as input -->
<!-- so the robot_state_publisher takes input from the /joint_states and URDF and updates the /tf topic which sends to other node from existing stack -->

ros2 run rviz2 rviz2 -d path_to_urdf_config.rviz