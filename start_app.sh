#! /usr/bin/env bash

PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

echo Debug output for ros tutorial gui

. /opt/ros/jazzy/setup.bash
. $PROJECT_ROOT/../install/install/setup.bash
. $PROJECT_ROOT/venv/bin/activate

export PYTHONPATH="$PROJECT_ROOT/venv/lib/python3.12/site-packages:$PYTHONPATH"

# if the app crash give ample time to read the error msg
ros2 run qt main || sleep 10s
