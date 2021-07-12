#! /usr/bin/env python3
import keyboard

from raerospy_radgripper_client.RadialgripperClient import RadialgripperClient
from raerospy_rack_client.RackClient import RackClient
from raerospy_vacmod_client.VacmodClient import VacmodClient
from raerospy_servo_client.ServoClient import ServoClient
import rospy,time



if __name__ == "__main__":
    rospy.init_node("example_py")
    gripper = RadialgripperClient()
    rack = RackClient()
    vacmod = VacmodClient()
    servo = ServoClient()

    # For callback return of vacuum state
    def sucked_cb():
        rospy.loginfo("Sucked an object!")
        gripper.grasp(current=1000)
        time.sleep(5)
        rack.to(0.06)
        vacmod.release()
        
    def lost_cb():
        rospy.loginfo("Lost an object!")
        lost = True

    servo.limp()

    calibration = input("Calibration needed? (Y|N)")

    if calibration.upper() == "Y":
        servo.limp()
        time.sleep(1)
        input("Unmount Grippers, insert Rack and then press enter")
        rack.home()
        rack.to(0.01)
        input("Mount Grippers, that both fingertips touch each other and then press Enter")
        gripper.calibrate()

    rack.to(0.06)
    
    try:
        while True:
            input("Press enter to start")
            vacmod.suck(sucked_cb,lost_cb)
            
  

    except KeyboardInterrupt:
        servo.limp()
        