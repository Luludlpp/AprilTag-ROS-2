# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag

# Utility rule file for apriltag_python.

# Include any custom commands dependencies for this target.
include CMakeFiles/apriltag_python.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/apriltag_python.dir/progress.make

CMakeFiles/apriltag_python: apriltag.cpython-310-x86_64-linux-gnu.so

apriltag.cpython-310-x86_64-linux-gnu.so: libapriltag.so.3.2.0
apriltag.cpython-310-x86_64-linux-gnu.so: apriltag_pywrap.o
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating apriltag.cpython-310-x86_64-linux-gnu.so"
	x86_64-linux-gnu-gcc -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -g -fwrapv -O2 -lpython3.10 -Wl,-Bsymbolic-functions -g -fwrapv -O2 -Wl,-rpath,lib apriltag_pywrap.o /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag/libapriltag.so.3.2.0 -o apriltag.cpython-310-x86_64-linux-gnu.so

apriltag_pywrap.o: /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag/apriltag_pywrap.c
apriltag_pywrap.o: apriltag_detect.docstring.h
apriltag_pywrap.o: apriltag_py_type.docstring.h
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating apriltag_pywrap.o"
	/usr/bin/cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -fPIC -I/usr/include/python3.10 -I/usr/lib/python3/dist-packages/numpy/core/include -Wno-strict-prototypes -I/home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag -c -o apriltag_pywrap.o /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag/apriltag_pywrap.c

apriltag_detect.docstring.h:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating apriltag_detect.docstring.h"
	< /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag/apriltag_detect.docstring sed 's/"/\\"/g; s/^/"/; s/$$/\\n"/;' > apriltag_detect.docstring.h

apriltag_py_type.docstring.h:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Generating apriltag_py_type.docstring.h"
	< /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag/apriltag_py_type.docstring sed 's/"/\\"/g; s/^/"/; s/$$/\\n"/;' > apriltag_py_type.docstring.h

apriltag_python: CMakeFiles/apriltag_python
apriltag_python: apriltag.cpython-310-x86_64-linux-gnu.so
apriltag_python: apriltag_detect.docstring.h
apriltag_python: apriltag_py_type.docstring.h
apriltag_python: apriltag_pywrap.o
apriltag_python: CMakeFiles/apriltag_python.dir/build.make
.PHONY : apriltag_python

# Rule to build all files generated by this target.
CMakeFiles/apriltag_python.dir/build: apriltag_python
.PHONY : CMakeFiles/apriltag_python.dir/build

CMakeFiles/apriltag_python.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/apriltag_python.dir/cmake_clean.cmake
.PHONY : CMakeFiles/apriltag_python.dir/clean

CMakeFiles/apriltag_python.dir/depend:
	cd /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/apriltag /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag /home/ben/mp3_ros2_ws/src/AprilTag-ROS-2/build/apriltag/CMakeFiles/apriltag_python.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/apriltag_python.dir/depend

