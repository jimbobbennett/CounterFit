'''
Provides a connection to the Virtual IoT Device server. This connection is re-used by all the virtual sensors.

Examples:

    When connecting to localhost on the default port:

    .. code-block:: python

        from virtualiot-shims-grove.virtual_iot_connection import VirtualIoTConnection

        VirtualIoTConnection.init()


    When connection to another computer on a different port:

    .. code-block:: python

        from virtualiot-shims-grove.virtual_iot_connection import VirtualIoTConnection

        VirtualIoTConnection.init('192.168.197.1', 5050)
'''
import requests

class VirtualIoTConnection:
    '''
    Connects to the Virtual IoT device on a give host and port, and allows the value of sensors to be read,
    as well as setting the value of actuators.
    '''
    base_url = ''

    @staticmethod
    def init(hostname: str = 'localhost', port: int = 5000) -> None:
        '''
        Initializes the connection to the Virtual IoT Device running on the given url and port
        '''
        VirtualIoTConnection.base_url = f'http://{hostname}:{str(port)}/'
    
    @staticmethod
    def get_sensor_float_value(pin: int) -> float:
        '''
        Reads a float value from the sensor on the given pin
        '''
        response = requests.get(VirtualIoTConnection.base_url + 'sensor_value?pin=' + str(pin))
        return float(response.json()['value'])
    
    @staticmethod
    def get_sensor_boolean_value(pin: int) -> bool:
        '''
        Reads a bool value from the sensor on the given pin
        '''
        response = requests.get(VirtualIoTConnection.base_url + 'sensor_value?pin=' + str(pin))
        return bool(response.json()['value'])
    
    @staticmethod
    def set_actuator_float_value(pin: int, value: float) -> None:
        '''
        Sends a float value to the actuator on the given pin
        '''
        requests.post(VirtualIoTConnection.base_url + 'actuator_value?pin=' + str(pin), json= {'value':value})
    
    @staticmethod
    def set_actuator_boolean_value(pin: int, value: bool) -> None:
        '''
        Sends a bool value to the actuator on the given pin
        '''
        requests.post(VirtualIoTConnection.base_url + 'actuator_value?pin=' + str(pin), json= {'value':value})
