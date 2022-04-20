#!/usr/bin/env python
from std_msgs.msg import String

import rospy
rospy.init_node('publisher')
p = rospy.Publisher('team_abhiyaan',String, queue_size=5)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	p.publish("Team Abhiyaan rocks")
	rate.sleep()
