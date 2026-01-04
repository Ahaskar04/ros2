// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_robot_interfaces:msg/LedPanelState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "my_robot_interfaces/msg/led_panel_state.hpp"


#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__LED_PANEL_STATE__STRUCT_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__LED_PANEL_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_robot_interfaces__msg__LedPanelState __attribute__((deprecated))
#else
# define DEPRECATED__my_robot_interfaces__msg__LedPanelState __declspec(deprecated)
#endif

namespace my_robot_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LedPanelState_
{
  using Type = LedPanelState_<ContainerAllocator>;

  explicit LedPanelState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int64_t, 3>::iterator, int64_t>(this->led_states.begin(), this->led_states.end(), 0ll);
    }
  }

  explicit LedPanelState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : led_states(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      std::fill<typename std::array<int64_t, 3>::iterator, int64_t>(this->led_states.begin(), this->led_states.end(), 0ll);
    }
  }

  // field types and members
  using _led_states_type =
    std::array<int64_t, 3>;
  _led_states_type led_states;

  // setters for named parameter idiom
  Type & set__led_states(
    const std::array<int64_t, 3> & _arg)
  {
    this->led_states = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_robot_interfaces::msg::LedPanelState_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_robot_interfaces::msg::LedPanelState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::msg::LedPanelState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_robot_interfaces::msg::LedPanelState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_robot_interfaces__msg__LedPanelState
    std::shared_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_robot_interfaces__msg__LedPanelState
    std::shared_ptr<my_robot_interfaces::msg::LedPanelState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LedPanelState_ & other) const
  {
    if (this->led_states != other.led_states) {
      return false;
    }
    return true;
  }
  bool operator!=(const LedPanelState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LedPanelState_

// alias to use template instance with default allocator
using LedPanelState =
  my_robot_interfaces::msg::LedPanelState_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__LED_PANEL_STATE__STRUCT_HPP_
