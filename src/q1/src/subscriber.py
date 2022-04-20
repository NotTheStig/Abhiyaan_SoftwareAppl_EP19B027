#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(msg):
	print(msg.data)
rospy.init_node('subscriber')
sub = rospy.Subscriber('team_abhiyaan',String, callback)
rospy.spin()
