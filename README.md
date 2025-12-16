# ros2

colcon build --packages-select my_py_pkg: always build from the ros2 directory 

source ~/.bashrc: then do this at the base directory 
After you create a node and build with colcon build, ROS doesn't automatically know about your new package. Sourcing "refreshes" your terminal so you can just restart your terminal as wwell.


ros2 run my_py_pkg py_node: package name and the executable node name which has been built

ros2 node list: gives all the running nodes 

--ros-args -r __node:=abc : change the name of a running node(allows to run same node multiple time simultaneously with different names)

**`colcon build --packages-select my_py_pkg`** (normal build)
- Copies your Python files to the `install/` folder
- After editing code, you must rebuild every time to see changes
- Files don't need to be executable

**`colcon build --packages-select my_py_pkg --symlink-install`** (symlink build)
- Creates symbolic links (shortcuts) pointing to your original source files
- After editing code, changes apply immediately — no rebuild needed
- Files must be executable (`chmod +x`)



rqt or rqt_graph: GUI for nodes 


turtlesim:
ros2 run turtlesim turtlesim_node
ros2 run turtlesim turtle_teleop_key


Topic:
A topic is a named bus over which nodes exachange messages 
- unidirectional data stream(publisher/subscriber)
- anonymous 
- a topic has a message type
- a node can have many publishers/subscribers fpr many different topics 
(remember the radio analogy)

ros2 topic list: to get the list of publishers 
ros2 topic echo /robot_news: to mimic the subscriber of the publisher



