cmake_minimum_required(VERSION 3.2)
project(Hyper)

SET(CMAKE_CXX_FLAGS "-std=c++14")

include_directories(include)

file(GLOB SOURCES "src/*.cpp")

add_executable(Hyper ${SOURCES})