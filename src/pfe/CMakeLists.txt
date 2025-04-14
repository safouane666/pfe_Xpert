cmake_minimum_required(VERSION 3.8)
project(pfe)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# C++ executable
add_executable(node2 src/node2.cc)
ament_target_dependencies(node2 rclcpp std_msgs)

# Install C++ node
install(TARGETS
  node2
  DESTINATION lib/${PROJECT_NAME}
)

# Install Python node
install(PROGRAMS
  src/node1.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

# Add Python dependencies if needed
find_package(ament_cmake_python REQUIRED)

ament_package()
