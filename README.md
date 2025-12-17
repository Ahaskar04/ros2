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
```

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