cmake_minimum_required(VERSION 3.16)
project(fibonacci)

# Setting C/CXX Default Standard
set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)

# Setting Default CMake build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()
message(STATUS "CMAKE BUILD TYPE: ${CMAKE_BUILD_TYPE}")


# Set Addition Flags
set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

add_executable("bin_main" "main.cpp")