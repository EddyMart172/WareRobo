"""
Eddy's Warehouse Robot - WareRobo
These are the definitions for the classes and functions for WareRobo
"""

"""
The main class for the warehouse Robot as a whole. 
"""
class Robot:
    def __init__(self, RoboID) -> None:
       self._Robot = [] # an array to hold the Robot
       self.RoboID = RoboID
    print("Robot constructor")

    def addRobot(self, newrobot) -> None:
        print("Add a new Robot to Warehouse")


# Starting point of application
# no guarantees -- I am not a programmer
if __name__ == "__main__":
    
    pass
# Create an instance of Robot
    # and call some methods 
    myrobot = Robot(RoboID=101)
    RoboID=(101)

from Motor import Motor
from PIR import PIR
