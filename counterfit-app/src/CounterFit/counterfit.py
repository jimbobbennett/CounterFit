import argparse
import json
import os
import webbrowser
from threading import Timer
from flask import Flask, request, render_template
from flask_socketio import SocketIO

from .sensors import SensorBase, SensorType
from .actuators import ActuatorBase

app = Flask(__name__)
app.config['SECRET_KEY'] = '247783f3-bdda-4536-bffc-109e2464f10b'
socketio = SocketIO(app)

sensor_cache = {}
actuator_cache = {}

all_sensors = []
all_actuators = []

def get_all_subclasses(cls, class_list):
    for sub_class in cls.__subclasses__():
        if len(sub_class.__abstractmethods__) == 0:
            class_list.append(sub_class)

        get_all_subclasses(sub_class, class_list)

get_all_subclasses(SensorBase, all_sensors)
get_all_subclasses(ActuatorBase, all_actuators)

@app.route('/', methods=['GET'])
def home():
    pins = []
    for pin in range(1, 19):
        if pin not in sensor_cache:
            pins.append(pin)

    return render_template('home.html', 
                           sensors=sensor_cache.values(),
                           actuators=actuator_cache.values(), 
                           all_sensors=all_sensors,
                           all_actuators=all_actuators,
                           pins=pins)

@app.route('/create_sensor', methods=['POST'])
def create_sensor():
    body = request.get_json()

    print("Create sensor called:", body)
    
    sensor_type = body['type']
    pin = body['pin']
    unit = body['unit']

    for sensor in all_sensors:
        if sensor.sensor_name() == sensor_type:
            if sensor.sensor_type() == SensorType.FLOAT:
                new_sensor = sensor(pin, unit)
            else:
                new_sensor = sensor(pin)

            sensor_cache[pin] = new_sensor

    return 'OK', 200

@app.route('/create_actuator', methods=['POST'])
def create_actuator():
    body = request.get_json()

    print("Create actuator called:", body)
    
    actuator_type = body['type']
    pin = body['pin']

    for actuator in all_actuators:
        if actuator.actuator_name() == actuator_type:
            new_actuator = actuator(pin)

            actuator_cache[pin] = new_actuator

    return 'OK', 200

@app.route('/sensor_value', methods=['GET'])
def get_sensor_value():
    pin = int(request.args.get('pin', ''))
    if pin in sensor_cache:
        sensor = sensor_cache[pin]
        
        response = {'value' : sensor.value}
        print("Returning sensor value", response, "for pin", pin)

        return json.dumps(response)
    
    return 'Sensor with pin ' + str(pin) + ' not found', 404

@app.route('/delete_sensor', methods=['POST'])
def delete_sensor():
    body = request.get_json()

    print("Delete sensor called:", body)

    pin = body['pin']

    if pin in sensor_cache:
        del sensor_cache[pin]

    return 'OK', 200

@app.route('/delete_actuator', methods=['POST'])
def delete_actuator():
    body = request.get_json()

    print("Delete actuator called:", body)

    pin = body['pin']

    if pin in actuator_cache:
        del actuator_cache[pin]

    return 'OK', 200

@app.route('/float_sensor_settings', methods=['POST'])
def set_float_sensor_settings():
    body = request.get_json()

    print("Float sensor settings called:", body)
    
    pin = body['pin']
    value = body['value']
    is_random = body['is_random']
    random_min = body['random_min']
    random_max = body['random_max']

    if pin in sensor_cache:
        sensor = sensor_cache[pin]
        sensor.value = value
        sensor.random = is_random
        sensor.random_min = random_min
        sensor.random_max = random_max

    return 'OK', 200

@app.route('/led_actuator_settings', methods=['POST'])
def set_led_actuator_settings():
    body = request.get_json()

    print("LED actuator settings called:", body)
    
    pin = body['pin']
    color = body['color']

    if pin in actuator_cache:
        actuator = actuator_cache[pin]
        actuator.color = color

    return 'OK', 200

@app.route('/boolean_sensor_settings', methods=['POST'])
def set_boolean_sensor_settings():
    body = request.get_json()

    print("Boolean sensor settings called:", body)
    
    pin = body['pin']
    value = body['value']
    is_random = body['is_random']

    if pin in sensor_cache:
        sensor = sensor_cache[pin]
        sensor.value = value
        sensor.random = is_random

    return 'OK', 200

@app.route('/sensor_units', methods=['POST'])
def get_sensor_units():
    body = request.get_json()

    print("Sensor units called:", body)

    sensor_type = body['type']

    for sensor in all_sensors:
        if sensor.sensor_name() == sensor_type:
            if sensor.sensor_type() == SensorType.FLOAT:
                return {'units':sensor.sensor_units()}

            return {'units':[]}

    return 'Not found', 404

@app.route('/actuator_value', methods=['POST'])
def set_actuator_value():
    pin = int(request.args.get('pin', ''))
    body = request.get_json()

    print("Actuator value called:", body)

    value = body['value']

    if pin in actuator_cache:
        actuator = actuator_cache[pin]
        actuator.value = value

        socketio.emit('actuator_change' + str(pin), {'pin':pin, 'value': value})

    return 'OK', 200

def open_browser(port):
    webbrowser.open_new(f'http://127.0.0.1:{port}/')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', metavar='port', type=int, default=5000, help='the port to run on')

    args = parser.parse_args()

    print(f'CounterFit - virtual IoT hardware running on port {args.port}')

    Timer(5, open_browser, [args.port]).start()
    
    socketio.run(app, port=args.port)

if __name__ == '__main__':
    main()
