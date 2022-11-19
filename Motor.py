"""
This is the Motor class. 
Motors control the motion, speed and direction of Robot
"""
class Motor:
    def __init__(self, Motor, MotorID) -> None:
        self._Motor = Motor # _Motor is the attribute for the motor
        self._MotorID = MotorID # _MotorID is the attribute for the ID number of the motor

    print ("Add a motor for our robot")
    print ("Add ID number for motor")

"""
   Start, stop, speed up, speed down for motor
"""
def MotorStart():
    print ("Motor Starting")

def MotorStop() :
    print ("Motor Stopping")

def SpeedUp() :
    print ("Motor Speed increase")

def SpeedDown() :
    print ("Motor Speed decrease")
