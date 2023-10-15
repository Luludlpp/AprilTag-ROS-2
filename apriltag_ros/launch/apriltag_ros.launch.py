# Copyright (c) 2023, Tinker Twins
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # run camera driver node
        ExecuteProcess(
            # NOTE: Change "mp3_ros2_ws" to what your workspace is !!!
            cmd=[['ros2 run usb_cam usb_cam_node_exe --ros-args --params-file ~/mp3_ros2_ws/src/AprilTag-ROS-2/usb_cam/config/params_2.yaml']],
            shell=True,
        ),
        # run image transport node
        ExecuteProcess(
            cmd=[['ros2 run image_transport republish compressed raw --ros-args --remap']],
            shell=True,
        ),
        # don't really know what this does...
        ExecuteProcess(
            cmd=[['run rqt_image_view rqt_image_view']],
            shell=True,
        ),
        # run april tag detection node
        ExecuteProcess(
            cmd=[['ros2 run apriltag_ros apriltag_node --ros-args -r image_rect:=/image_raw -r camera_info:=/camera_info --params-file `ros2 pkg prefix apriltag_ros`/share/apriltag_ros/cfg/tags_36h11.yaml']],
            shell=True,
        ),
        # run rviz2 vizualizer
        Node(
            package='rviz2',
            executable='rviz2',
            name='apriltag_rviz',
            arguments=['-d', [FindPackageShare("apriltag_ros"), '/rviz', '/apriltag.rviz',]]
        ),
    ])
