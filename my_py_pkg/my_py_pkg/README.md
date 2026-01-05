## Project 1: Robot News Station

**Concept:** Basic Topic Publisher/Subscriber pattern

| File                    | Role       | Description                                                 |
| ----------------------- | ---------- | ----------------------------------------------------------- |
| `robot_news_station.py` | Publisher  | Publishes "Hello" messages to `robot_news` topic every 0.5s |
| `smartphone.py`         | Subscriber | Listens to `robot_news` topic and logs received messages    |

**How to run:**

```bash
# Terminal 1
ros2 run my_py_pkg robot_news_station

# Terminal 2
ros2 run my_py_pkg smartphone
```

---

## Project 2: Number Counter

**Concept:** Topic communication with parameters + Service server

| File                | Role                | Description                                                                                                                         |
| ------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `number.py`         | Publisher           | Publishes a configurable number to `number` topic. Supports `number` and `time_period` parameters                                   |
| `number_counter.py` | Subscriber + Server | Subscribes to `number`, maintains a running sum, publishes to `number_count`. Also provides `add_two_ints` service to reset counter |

**How to run:**

```bash
# Terminal 1 - with custom parameters
ros2 run my_py_pkg number --ros-args -p number:=5 -p time_period:=0.5

# Terminal 2
ros2 run my_py_pkg number_counter
```

---

## Project 3: Add Two Ints Service

**Concept:** Service Client/Server pattern

| File                            | Role             | Description                                            |
| ------------------------------- | ---------------- | ------------------------------------------------------ |
| `add_two_ints_server.py`        | Server           | Provides `add_two_ints` service that adds two integers |
| `add_two_ints_client.py`        | Client (OOP)     | Calls the service asynchronously using callbacks       |
| `add_two_ints_client_no_oop.py` | Client (non-OOP) | Alternative implementation without OOP pattern         |

**How to run:**

```bash
# Terminal 1
ros2 run my_py_pkg add_two_ints_server

# Terminal 2
ros2 run my_py_pkg add_two_ints_client
```

**Test via CLI:**

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 3, b: 7}"
```

---

## Project 4: LED Panel & Battery

**Concept:** Service pattern with custom interfaces + state publishing

| File           | Role               | Description                                                                                 |
| -------------- | ------------------ | ------------------------------------------------------------------------------------------- |
| `Led_panel.py` | Server + Publisher | Manages LED state array, provides `set_led` service, publishes state to `led_panel_state`   |
| `battery.py`   | Client             | Simulates battery drain/charge cycle, calls `set_led` to toggle LED based on battery status |

**Dependencies:** Requires `my_robot_interfaces` package (custom `SetLed` service and `LedPanelState` message)

**How to run:**

```bash
# Terminal 1
ros2 run my_py_pkg Led_panel

# Terminal 2
ros2 run my_py_pkg battery
```

**Behavior:** Battery toggles between full (4s) and empty (6s), turning LED 0 on/off accordingly.

---

## Project 5: Turtle Chase Game

**Concept:** Multi-node system with turtlesim integration

| File            | Role                   | Description                                                                                                                   |
| --------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `spawner.py`    | Spawner + Publisher    | Calls turtlesim `/spawn` service every 3s, publishes alive turtles to `turtle_list`                                           |
| `controller.py` | Subscriber + Publisher | Subscribes to `turtle_list` and `/turtle1/pose`, calculates nearest turtle, publishes velocity commands to `/turtle1/cmd_vel` |

**Dependencies:** Requires `turtlesim` package and `my_robot_interfaces` (custom `Turtle` and `TurtleArray` messages)

**How to run:**

```bash
# Terminal 1 - Start turtlesim
ros2 run turtlesim turtlesim_node

# Terminal 2 - Start spawner
ros2 run my_py_pkg spawner

# Terminal 3 - Start controller
ros2 run my_py_pkg controller
```

**Behavior:** Turtles spawn randomly, turtle1 chases and catches the nearest one.

---

## Standalone/Utility Files

| File                           | Description                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| `my_first_node.py`             | Basic "Hello World" node for getting started                                         |
| `template_node.py`             | Boilerplate template for creating new nodes                                          |
| `hardware_status_publisher.py` | Demo publisher using custom `HardwareStatus` message (no subscriber in this package) |

---

## Quick Reference: Communication Patterns

| Pattern                 | Example Project                          |
| ----------------------- | ---------------------------------------- |
| Topic (Pub/Sub)         | Robot News, Number Counter               |
| Service (Client/Server) | Add Two Ints, LED Panel                  |
| Parameters              | Number publisher                         |
| Custom Interfaces       | LED Panel, Turtle Chase, Hardware Status |
| Turtlesim Integration   | Turtle Chase                             |
