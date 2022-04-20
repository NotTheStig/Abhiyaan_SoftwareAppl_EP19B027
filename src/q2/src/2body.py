#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

#The following code is not a full implementation of the problem statement. This code, obtained from ros wiki, just moves the turtlebot from its current location to a predetermined goal.
#The idea is to discretise the 2 body problem into small timesteps. In each timestep the turtles will move in a straight line, their direction and speed determined by their velocity vector.
#At the end of each timestep, the velocity vectors will be updated according to the acceleration vector (ΔV=AΔt). These updated velocity vectors will then be used for the next timestep.
#I was unable to implement this into code due to time constraint (the given time was enough but I had other obligations)


class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        goal_pose = Pose()
        goal_pose.x = float(input("Set your x goal: "))
        goal_pose.y = float(input("Set your y goal: "))
        distance_tolerance = float(input("Set your tolerance: "))

        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        rospy.spin()

if __name__ == '__main__':
    try:
        t1 = TurtleBot()
        t1.move2goal()
        #t2= TurtleBot()
        #t2.move2goal()
    except rospy.ROSInterruptException:
        pass
