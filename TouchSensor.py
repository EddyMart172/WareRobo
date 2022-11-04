"""
Touch Bar Sensor is a subclass of Sensor
for defining the Touch Sensors used for 
Obstacle detection in the robots
"""
from Sensor import Sensor
class TouchBar(Sensor):

    def __init__(self, Sensortype, SensorID) -> None:
        super().__init__(Sensortype, SensorID)
        print("Define Touch Bar sensor")