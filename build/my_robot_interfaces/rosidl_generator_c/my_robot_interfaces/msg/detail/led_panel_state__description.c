// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from my_robot_interfaces:msg/LedPanelState.idl
// generated code does not contain a copyright notice

#include "my_robot_interfaces/msg/detail/led_panel_state__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_my_robot_interfaces
const rosidl_type_hash_t *
my_robot_interfaces__msg__LedPanelState__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xef, 0x97, 0xd1, 0xe8, 0x9b, 0x9e, 0xc6, 0xc2,
      0x79, 0x8f, 0x5b, 0x8b, 0x96, 0xe9, 0x6a, 0xf4,
      0xfe, 0xb6, 0x7a, 0xb2, 0x9e, 0x4b, 0x21, 0x35,
      0xfa, 0x62, 0x1a, 0x27, 0xaf, 0x35, 0x6b, 0xa9,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char my_robot_interfaces__msg__LedPanelState__TYPE_NAME[] = "my_robot_interfaces/msg/LedPanelState";

// Define type names, field names, and default values
static char my_robot_interfaces__msg__LedPanelState__FIELD_NAME__led_states[] = "led_states";

static rosidl_runtime_c__type_description__Field my_robot_interfaces__msg__LedPanelState__FIELDS[] = {
  {
    {my_robot_interfaces__msg__LedPanelState__FIELD_NAME__led_states, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT64_ARRAY,
      3,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
my_robot_interfaces__msg__LedPanelState__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {my_robot_interfaces__msg__LedPanelState__TYPE_NAME, 37, 37},
      {my_robot_interfaces__msg__LedPanelState__FIELDS, 1, 1},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "int64[3] led_states";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
my_robot_interfaces__msg__LedPanelState__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {my_robot_interfaces__msg__LedPanelState__TYPE_NAME, 37, 37},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 19, 19},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
my_robot_interfaces__msg__LedPanelState__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *my_robot_interfaces__msg__LedPanelState__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
