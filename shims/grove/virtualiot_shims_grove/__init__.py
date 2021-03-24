'''
Virtual IoT Device shims for Grove sensors.

This library provides shims that mimic the Grove Python libraries from:
    https://github.com/Seeed-Studio/grove.py

These shims don't communicate with real hardware, instead they communicate with a running instace of
the Virtual IoT Device app
'''

from .virtual_iot_connection import VirtualIoTConnection
from .grove_light_sensor_v1_2 import GroveLightSensor
from .grove_led import GroveLed
