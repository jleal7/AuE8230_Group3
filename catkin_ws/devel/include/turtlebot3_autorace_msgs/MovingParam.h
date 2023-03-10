// Generated by gencpp from file turtlebot3_autorace_msgs/MovingParam.msg
// DO NOT EDIT!


#ifndef TURTLEBOT3_AUTORACE_MSGS_MESSAGE_MOVINGPARAM_H
#define TURTLEBOT3_AUTORACE_MSGS_MESSAGE_MOVINGPARAM_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace turtlebot3_autorace_msgs
{
template <class ContainerAllocator>
struct MovingParam_
{
  typedef MovingParam_<ContainerAllocator> Type;

  MovingParam_()
    : moving_type(0)
    , moving_value_angular(0.0)
    , moving_value_linear(0.0)  {
    }
  MovingParam_(const ContainerAllocator& _alloc)
    : moving_type(0)
    , moving_value_angular(0.0)
    , moving_value_linear(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _moving_type_type;
  _moving_type_type moving_type;

   typedef float _moving_value_angular_type;
  _moving_value_angular_type moving_value_angular;

   typedef float _moving_value_linear_type;
  _moving_value_linear_type moving_value_linear;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(MOVING_TYPE_IDLE)
  #undef MOVING_TYPE_IDLE
#endif
#if defined(_WIN32) && defined(MOVING_TYPE_LEFT)
  #undef MOVING_TYPE_LEFT
#endif
#if defined(_WIN32) && defined(MOVING_TYPE_RIGHT)
  #undef MOVING_TYPE_RIGHT
#endif
#if defined(_WIN32) && defined(MOVING_TYPE_FORWARD)
  #undef MOVING_TYPE_FORWARD
#endif
#if defined(_WIN32) && defined(MOVING_TYPE_BACKWARD)
  #undef MOVING_TYPE_BACKWARD
#endif

  enum {
    MOVING_TYPE_IDLE = 0u,
    MOVING_TYPE_LEFT = 1u,
    MOVING_TYPE_RIGHT = 2u,
    MOVING_TYPE_FORWARD = 3u,
    MOVING_TYPE_BACKWARD = 4u,
  };


  typedef boost::shared_ptr< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> const> ConstPtr;

}; // struct MovingParam_

typedef ::turtlebot3_autorace_msgs::MovingParam_<std::allocator<void> > MovingParam;

typedef boost::shared_ptr< ::turtlebot3_autorace_msgs::MovingParam > MovingParamPtr;
typedef boost::shared_ptr< ::turtlebot3_autorace_msgs::MovingParam const> MovingParamConstPtr;

// constants requiring out of line definition

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator1> & lhs, const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator2> & rhs)
{
  return lhs.moving_type == rhs.moving_type &&
    lhs.moving_value_angular == rhs.moving_value_angular &&
    lhs.moving_value_linear == rhs.moving_value_linear;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator1> & lhs, const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace turtlebot3_autorace_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
{
  static const char* value()
  {
    return "603d953881321b4196ac96fba411105f";
  }

  static const char* value(const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x603d953881321b41ULL;
  static const uint64_t static_value2 = 0x96ac96fba411105fULL;
};

template<class ContainerAllocator>
struct DataType< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
{
  static const char* value()
  {
    return "turtlebot3_autorace_msgs/MovingParam";
  }

  static const char* value(const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
{
  static const char* value()
  {
    return "########################################\n"
"# CONSTANTS\n"
"########################################\n"
"uint8 MOVING_TYPE_IDLE = 0\n"
"uint8 MOVING_TYPE_LEFT = 1\n"
"uint8 MOVING_TYPE_RIGHT = 2\n"
"uint8 MOVING_TYPE_FORWARD = 3\n"
"uint8 MOVING_TYPE_BACKWARD = 4\n"
"\n"
"########################################\n"
"# Messages\n"
"########################################\n"
"uint8 moving_type\n"
"float32 moving_value_angular\n"
"float32 moving_value_linear\n"
;
  }

  static const char* value(const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.moving_type);
      stream.next(m.moving_value_angular);
      stream.next(m.moving_value_linear);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MovingParam_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::turtlebot3_autorace_msgs::MovingParam_<ContainerAllocator>& v)
  {
    s << indent << "moving_type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.moving_type);
    s << indent << "moving_value_angular: ";
    Printer<float>::stream(s, indent + "  ", v.moving_value_angular);
    s << indent << "moving_value_linear: ";
    Printer<float>::stream(s, indent + "  ", v.moving_value_linear);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TURTLEBOT3_AUTORACE_MSGS_MESSAGE_MOVINGPARAM_H
