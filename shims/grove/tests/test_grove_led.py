'''
Tests the Grove LED sensor shim.

To run this test, ensure you have the Virtual IoT Device app running, with an LED actuator
on pin 1

'''
# pylint: disable=redefined-outer-name,unused-argument

import pytest

from virtualiot_shims_grove.virtual_iot_connection import VirtualIoTConnection
from virtualiot_shims_grove.grove_led import GroveLed

@pytest.fixture
def init_virtual_iot_device():
    '''
    Test fixture to initialise the connection to the Virtual IoT device running on localhost on port 5000
    '''
    VirtualIoTConnection.init('127.0.0.1', 5000)

def test_turn_led_on(init_virtual_iot_device):
    '''
    Tests the on method of the Grove LED shim
    '''
    sensor = GroveLed(1)
    sensor.on()

def test_turn_led_off(init_virtual_iot_device):
    '''
    Tests the off method of the Grove LED shim
    '''
    sensor = GroveLed(1)
    sensor.off()
