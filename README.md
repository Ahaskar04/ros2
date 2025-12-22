# ROS2 Quick Reference Guide

## Building Packages

```bash
# Build a specific package (run from ros2_ws directory)
colcon build --packages-select my_py_pkg

# Source your environment after building
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

```bash
# Run a node (package_name followed by executable_name)
ros2 run my_py_pkg py_node

# List all running nodes
ros2 node list

# Run a node with a custom name (allows multiple instances)
ros2 run my_py_pkg py_node --ros-args -r __node:=abc
```

---

## Visualization Tools

```bash
# Launch ROS2 GUI tools
rqt
rqt_graph

---

## Turtlesim (Demo Package)

```bash
# Launch the turtlesim window
ros2 run turtlesim turtlesim_node

# Control the turtle with keyboard
ros2 run turtlesim turtle_teleop_key
```

---

## Topics

A **topic** is a named bus over which nodes exchange messages.

**Key characteristics:**
- Unidirectional data stream (publisher/subscriber model)
- Anonymous communication
- Each topic has a specific message type
- A node can have many publishers/subscribers for different topics

> *Think of it like a radio station: publishers broadcast, subscribers tune in.*

### Topic Commands

```bash
# List all active topics
ros2 topic list

# Subscribe to a topic and print messages
ros2 topic echo /robot_news

# Get topic info (type, publisher/subscriber count)
ros2 topic info /robot_news
```

**Example output:**
```
Type: example_interfaces/msg/String
Publisher count: 1
Subscription count: 0
```

```bash
# Show message type definition
ros2 interface show example_interfaces/msg/String

# Check publishing frequency
ros2 topic hz /robot_news

# Check bandwidth usage
ros2 topic bw /robot_news
```

### Remapping Topics

```bash
# Remap both node name and topic name
ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=abc
```

> **Important:** If you remap a publisher's topic, you must also remap the subscriber to match!

ros2 bag record /topic_name: record the data from the topic
ros2 bag info test 
ros2 bag play test: replay and publishes all the data that was published in the topic
ros2 bag play *the recording name*: acts as the publisher which you recorded 
ros2 bag record -o test2 /topic1 /topic2: recording name is test2 and is recording 2 topics 
ros2 bag record -o test3 -a: to record all the topics 

Service:
a ROS2 service is a client/server system 
asynchronous/synchromous
one msg type for request, one msg type for response 
a service server can only exist once but can have many clients 
a service is defiened ny its name and interface
ahaskar@ros2:~$ ros2 interface show example_interfaces/srv/AddTwoInts
int64 a
int64 b
---
int64 sum


ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts {"a: 3, b: 7"}
: to test a server through the terminal(making a client through the terminal)

ros2 service list
ros2 service type /service_name: same thing as ros2 node info 
ros2 run my_py_pkg file_name --ros-args -r old_server_name:=new_server_name
(*also need to rename the service on the client side if you rename a server service name*)


Interfaces:
built on basic primitive data types 
all example interfaces: https://github.com/ros2/example_interfaces
https://github.com/ros2/common_interfaces
seonsor_msg interface really helpful 

ros2 pkg create my_robot_interfaces 

ros2 interface list: all the interfaces sourced 

ros2 interface package my_robot_interfaces: all the interfaces for for my_robot_interfaces


ros2 run my_py_pkg number --ros-args -p number:=3 -p timer_period:=0.5  :to set parameters 