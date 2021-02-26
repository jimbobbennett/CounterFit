import sensors
import json
from flask import Flask, request, render_template

app = Flask(__name__)

sensor_cache = {}

all_sensors = []

def get_all_subclasses(c, class_list):
    for sub_class in c.__subclasses__():
        if len(sub_class.__abstractmethods__) == 0:
            class_list.append(sub_class)

        get_all_subclasses(sub_class, class_list)

get_all_subclasses(sensors.SensorBase, all_sensors)

@app.route('/', methods=['GET'])
def home():
    pins = []
    for pin in range(1, 19):
        if pin not in sensor_cache:
            pins.append(pin)

    return render_template('home.html', sensors=sensor_cache.values(), all_sensors=all_sensors, pins=pins)

@app.route('/create_sensor', methods=['POST'])
def create_sensor():
    body = request.get_json()

    print("Create sensor called:", body)
    
    sensor_type = body['type']
    pin = body['pin']
    unit = body['unit']

    for sensor in all_sensors:
        if sensor.sensor_name() == sensor_type:
            if sensor.sensor_type() == sensors.SensorType.Float:
                new_sensor = sensor(pin, unit)
            else:
                new_sensor = sensor(pin)

            sensor_cache[pin] = new_sensor

    return 'OK', 200


@app.route('/sensor_value', methods=['GET'])
def get_sensor_value():
    pin = int(request.args.get('pin', ''))
    if pin in sensor_cache:
        sensor:sensors.Sensor = sensor_cache[pin]
        
        response = {'value' : sensor.value}
        print("Returning sensor value", response, "for pin", pin)

        return json.dumps(response)
    
    return 'Sensor with pin ' + pin + ' not found', 404

@app.route('/delete_sensor', methods=['POST'])
def delete_sensor():
    body = request.get_json()

    print("Delete sensor called:", body)

    pin = body['pin']

    if pin in sensor_cache:
        del sensor_cache[pin]

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
        sensor:sensors.Sensor = sensor_cache[pin]
        sensor.value = value
        sensor.random = is_random
        sensor.random_min = random_min
        sensor.random_max = random_max

    return 'OK', 200

@app.route('/boolean_sensor_settings', methods=['POST'])
def set_boolean_sensor_settings():
    body = request.get_json()

    print("Boolean sensor settings called:", body)
    
    pin = body['pin']
    value = body['value']
    is_random = body['is_random']

    if pin in sensor_cache:
        sensor:sensors.Sensor = sensor_cache[pin]
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
            if sensor.sensor_type() == sensors.SensorType.Float:
                return {'units':sensor.sensor_units()}
            else:
                return {'units':[]}

    return 'Not found', 404