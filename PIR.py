"""
PIR is a subclass of Sensor
for defining the Passive Infrared Sensors used for 
Obstacle detection in the robots
"""
from Sensor import Sensor
class PIR(Sensor):

    def __init__(self, Sensortype, SensorID) -> None:
        super().__init__(Sensortype, SensorID)
        print("Define PIR sensor")
        Sensortype=PIR
        SensorID='23'
        