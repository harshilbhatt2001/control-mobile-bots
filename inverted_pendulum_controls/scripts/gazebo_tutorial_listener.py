#!/usr/bin/env python

import rospy
from controls.msg import inverted_pendulum_states


def chatterCallback(msg):
    torque = msg.wheel_torques
    angle = msg.pendulum_angle
    angle_velocity = msg.pendulum_angle_velocity
    speed = msg.chasis_speed
    rospy.loginfo("%f,%f,%f,%f\n", torque, angle, angle_velocity, speed)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("pendulum_states",
                     inverted_pendulum_states, chatterCallback)
    rospy.spin()


if __name__ == "__main__":
    listener()
