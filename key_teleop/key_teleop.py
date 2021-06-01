#!/usr/bin/env python

import rospy
#import Twist ใช้สำหรับ return ค่า liner and angular
from geometry_msgs.msg import Twist

message = """

Control 
---------------------------
Moving around:

 - for left hand :          - for right hand :
        w                           i
   a    s    d                  j   k   l
        
w/i : move forward
s/k : move backward
a/j : turn left
d/l : turn right
space key : stop moving
q to quit

"""

def key_teleop():
    #กำหนด topic='key_teleop' และโหนดที่เป็น publish='keyboard'
    pub = rospy.Publisher('key_teleop',Twist,queue_size=10)
    rospy.init_node('keyboard',anonymous=True)
    rate = rospy.Rate(10)
    move = Twist()

    while not rospy.is_shutdown():
	#รับค่าจากคีย์บอร์ด และสร้าง condition ต่างๆสำรับแยกแยะว่าแป้นพิมที่ถูกกดเข้ามาคือตัวอักษรใด ถ้าหากเดินหน้า/ถอยหลัง จะทำการกำหนดค่า linear.x แต่ถ้าเลี้ยวซ้ายหรือ/ขวาจะทำการกำหนด angular.z ทิศทางข้างหน้า/ด้านขวาเป็นค่าบวก
        key = input()
        
        if (key == "w") or (key == "i") :
            move.linear.x = 0.05
            print("move forward : \nlinear velocity = %f \nangular velocity = %f " % (move.linear.x, move.angular.z))
        elif (key == 'a') or (key == 'j') :
            move.angular.z = 0.2
            print("turn left : \nlinear velocity = %f \nangular velocity = %f " % (move.linear.x, move.angular.z))
        elif (key == 'd') or (key == 'l') :
            move.angular.z = -0.2
            print("turn right : \nlinear velocity = %f \nangular velocity = %f " % (move.linear.x, move.angular.z))
        elif (key == 'k') or (key == 's') :
            move.linear.x = -0.05
            print("stop moving : \nlinear velocity = %f \nangular velocity = %f " % (move.linear.x, move.angular.z))
	elif (key == ' ') :
            move.linear.x = 0.0
            move.angular.z = 0.0
            print("stop moving : \nlinear velocity = %f \nangular velocity = %f " % (move.linear.x, move.angular.z))
        elif key == 'q':
            break
        else:
            move.linear.x = 0.0
            move.angular.z = 0.0
        
        pub.publish(move)
        rate.sleep()


if __name__ == "__main__":
    
    try:
	#print message เพื่อบอกผู้ใช้งานว่าควรกดแป้นใด
        print(message)
        key_teleop()

    except rospy.ROSInterruptException:
        pass
