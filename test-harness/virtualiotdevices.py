import requests

class TemperatureSensor():
    def __init__(self, pin:int, port:int = 5000, hostname:str = '127.0.0.1'):
        self.__hostname = hostname
        self.__port = port
        self.__pin = pin

        print('Creating temperature sensor with pin:', self.__pin)
    
    def value(self) -> float:
        response = requests.get('http://' + self.__hostname + ':' + str(self.__port) + '/sensor_value?pin=' + str(self.__pin))
        return float(response.json()['value'])

class PressureSensor():
    def __init__(self, pin:int, port:int = 5000, hostname:str = '127.0.0.1'):
        self.__hostname = hostname
        self.__port = port
        self.__pin = pin

        print('Creating pressure sensor with pin:', self.__pin)
    
    def value(self) -> float:
        response = requests.get('http://' + self.__hostname + ':' + str(self.__port) + '/sensor_value?pin=' + str(self.__pin))
        return float(response.json()['value'])


class Button():
    def __init__(self, pin:int, port:int = 5000, hostname:str = '127.0.0.1'):
        self.__hostname = hostname
        self.__port = port
        self.__pin = pin

        print('Creating button with pin:', self.__pin)
    
    def value(self) -> bool:
        response = requests.get('http://' + self.__hostname + ':' + str(self.__port) + '/sensor_value?pin=' + str(self.__pin))
        return bool(response.json()['value'])
