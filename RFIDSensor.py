"""
RFIDSensor is a subclass of Sensor
for defining the Passive Infrared Sensors used for 
Obstacle detection in the robots
"""
from Sensor import Sensor
class RFIDSensor(Sensor):

    def __init__(self, Sensortype, SensorID) -> None:
        super().__init__(Sensortype, SensorID)
        print("Define RFID sensor")