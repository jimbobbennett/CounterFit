import asyncio
from virtualiotdevices import Button, PressureSensor, TemperatureSensor

temp_sensor = TemperatureSensor(1)
pressure_sensor = PressureSensor(2)
button = Button(3)

async def main():
    while True:
        if (button.value()):
            print("Button pressed - Temperature:", temp_sensor.value(), "Pressure:", pressure_sensor.value())
        else:
            print("Button not pressed")

        # Wait for a minute so telemetry is not sent to often
        await asyncio.sleep(5)

# Start the program running
asyncio.run(main())