#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
import math

global pub

# the converter
def quat_to_deg(data):
    global pub

    # storing the values
    x = data.orientation.x
    y = data.orientation.y
    z = data.orientation.z
    w = data.orientation.z

    # calculate the yaw , pitch and roll angls from thq quaternion
    yaw = math.atan2(2*(w*z + x*y) , 1 - 2*(y*y + z*z))
    pitch = math.asin(2*(w*y - z*x))
    roll = math.atan2(2*(w*x + y*z) , 1 - 2*(x*x + y*y))

    # covert Euler angles to degrees
    yaw_degrees = math.degrees(yaw)
    pitch_degrees = math.degrees(pitch)
    roll_degrees = math.degrees(roll)

    # publish the degrees
    pub.publish(Vector3(yaw_degrees , pitch_degrees , roll_degrees))

    rospy.loginfo(Vector3(yaw_degrees , pitch_degrees , roll_degrees))




def main():
    global pub
    # inilization of the node
    rospy.init_node("imu_converter")
    # subscriber to topic (/imu)
    sub = rospy.Subscriber("/imu" , Imu , quat_to_deg)
    # publisher to topic (imu_degrees)
    pub = rospy.Publisher("imu_degrees" , Vector3 ,queue_size=10)
    rospy.spin()




if __name__ == "__main__":
    while not rospy.is_shutdown():
        main()
