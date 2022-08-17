#!/usr/bin/env python3
import subprocess
import rospy
import os

rospy.init_node("gui")


bashCommand = "yarn serve"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()