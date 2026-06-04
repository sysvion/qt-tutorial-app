#! /usr/bin/env bash

echo Debug output for ros tutorial gui
. /opt/ros/jazzy/setup.bash
. ~/gui_ws/install/setup.bash
. ~/gui_ws/venv/bin/activate
export PYTHONPATH="/home/practicum/gui_ws/venv/lib/python3.12/site-packages:$PYTHONPATH"
ros2 run qt main || sleep 10s
