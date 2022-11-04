"""
This is the Sensor master class
"""
class Sensor:
    def __init__(self, Sensortype, SensorID) -> None:
        self._SensorType = Sensortype # _sensortype is the attribute for the type of sensor PIR, touch, RFID
        self._SensorID = SensorID # _sensorID is the attribute for the ID number of the sensor

    print ("Add a type of sensor for our robot")
    print ("Add ID number for sensor")


