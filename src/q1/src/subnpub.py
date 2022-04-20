#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(msg):
	s=""
	for i in msg.data.split():
		s=s+i[::-1]+" "
	print(s)
rospy.init_node('subnpub')
sub = rospy.Subscriber('team_abhiyaan',String, callback)
pub = rospy.Publisher('naayibha_maet',String, queue_size=5)
rospy.spin()
