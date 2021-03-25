from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import random

class SensorType(Enum):
    FLOAT = 1
    BOOLEAN = 2

class SensorBase(ABC):
    def __init__(self, pin:int):
        self.__pin = pin
        self._random = False
    
    @staticmethod
    @abstractmethod
    def sensor_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def sensor_type() -> SensorType:
        pass

    @property
    def pin(self) -> int:
        return self.__pin
    
    @property
    def random(self) -> bool:
        return self._random

    @random.setter
    def random(self, val: bool):
        self._random = val

#pylint: disable=C0103
class DefaultUnit(Enum):
    NoUnits = 1

class FloatSensorBase(SensorBase):
    def __init__(self, pin:int, valid_min:float, valid_max:float):

        super().__init__(pin)

        self.__valid_min = valid_min
        self.__valid_max = valid_max
        self.value = valid_min
        self.random_min = float(valid_min)
        self.random_max = float(valid_max)

    @staticmethod
    @abstractmethod
    def sensor_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def sensor_units() -> List[str]:
        pass

    @property
    @abstractmethod
    def unit(self) -> str:
        pass

    @staticmethod
    def sensor_type() -> SensorType:
        return SensorType.FLOAT

    @property
    def value(self) -> float:
        if self._random:
            return round(random.uniform(self.__random_min, self.__random_max), 2)

        return self.__value

    @value.setter
    def value(self, val: float):
        if val < self.__valid_min or val > self.__valid_max:
            raise ValueError()
        self.__value = val

    @property
    def random_min(self) -> float:
        return self.__random_min

    @random_min.setter
    def random_min(self, val: float):
        if val < self.__valid_min or val > self.__valid_max:
            raise ValueError()
        self.__random_min = val

    @property
    def random_max(self) -> float:
        return self.__random_max

    @random_max.setter
    def random_max(self, val: float):
        if val < self.__valid_min or val > self.__valid_max:
            raise ValueError()
        self.__random_max = val

    @property
    def valid_min(self) -> float:
        return self.__valid_min

    @property
    def valid_max(self) -> float:
        return self.__valid_max

class BooleanSensorBase(SensorBase):
    def __init__(self, pin:int):

        super().__init__(pin)

        self.value = False

    @staticmethod
    @abstractmethod
    def sensor_name() -> str:
        pass

    @staticmethod
    def sensor_type() -> SensorType:
        return SensorType.BOOLEAN

    @property
    def value(self) -> bool:
        if self._random:
            return random.choice([True, False])

        return self.__value

    @value.setter
    def value(self, val: bool):
        self.__value = val

#pylint: disable=C0103
class TemperatureUnit(Enum):
    Celsius = 1
    Fahrenheit = 2
    Kelvin = 3

class TemperatureSensor(FloatSensorBase):
    def __init__(self, pin:int, unit):
        if isinstance (unit, str):
            unit = TemperatureUnit[unit]

        self.__unit = unit

        if self.__unit == TemperatureUnit.Celsius:
            valid_min = -273.15
        elif self.__unit == TemperatureUnit.Fahrenheit:
            valid_min = -459.67
        else:
            valid_min = 0
        
        super().__init__(pin, valid_min, 999999999.0)

    @staticmethod
    def sensor_name() -> str:
        return 'Temperature'

    @property
    def unit(self) -> str:
        return self.__unit.name

    @staticmethod
    def sensor_units() -> List[str]:
        return [TemperatureUnit.Celsius.name, TemperatureUnit.Fahrenheit.name, TemperatureUnit.Kelvin.name]

#pylint: disable=C0103,C0102
class PressureUnit(Enum):
    kPa = 1
    torr = 2
    atm = 3
    bar = 4

class PressureSensor(FloatSensorBase):
    def __init__(self, pin:int, unit):
        if isinstance (unit, str):
            unit = PressureUnit[unit]

        self.__unit = unit

        super().__init__(pin, 0, 999999999.0)

    @staticmethod
    def sensor_name() -> str:
        return 'Pressure'

    @property
    def unit(self) -> str:
        return self.__unit.name

    @staticmethod
    def sensor_units() -> List[str]:
        return [PressureUnit.kPa.name, PressureUnit.torr.name, PressureUnit.atm.name, PressureUnit.bar.name]

class LightSensor(FloatSensorBase):
    #pylint: disable=W0613
    def __init__(self, pin:int, unit):

        super().__init__(pin, 0, 1000)

    @staticmethod
    def sensor_name() -> str:
        return 'Light'

    @property
    def unit(self) -> str:
        return DefaultUnit.NoUnits.name

    @staticmethod
    def sensor_units() -> List[str]:
        return [DefaultUnit.NoUnits.name]

class ButtonSensor(BooleanSensorBase):
    @staticmethod
    def sensor_name() -> str:
        return 'Button'
