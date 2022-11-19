"""
This is the Sensor master class. 
Sensors include Passive Infrared (PIR)
Touch sensor and RFID
"""
class Sensor:
    def __init__(self, Sensortype, SensorID) -> None:
        self._SensorType = Sensortype # _sensortype is the attribute for the type of sensor PIR, touch, RFID
        self._SensorID = SensorID # _sensorID is the attribute for the ID number of the sensor

    print ("Add a type of sensor for our robot")
    print ("Add ID number for sensor")

"""
    Detect obstacles and/or determine location depending on type of sensor.
"""
def Detect():
    print ("Detecting")

"""
Signal robot to stop

"""
def SignalStop() :
    print ("Robot Stop signal issued")
"""
Signal robot to reverse
"""
def SignalReverse() :
    print ("Robot Reverse signal issued")

