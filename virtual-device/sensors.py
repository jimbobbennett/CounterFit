from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import random

class SensorType(Enum):
    Float = 1
    Boolean = 2

class SensorBase(ABC):
    def __init__(self, pin:int):
        self.__pin = pin
        self.random = False
    
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
    def random(self, v: bool):
        self._random = v

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
    def unit() -> str:
        pass

    @staticmethod
    def sensor_type() -> SensorType:
        return SensorType.Float

    @property
    def value(self) -> float:
        if self._random:
            return round(random.uniform(self._random_min, self._random_max), 2)

        return self._value

    @value.setter
    def value(self, v: float):
        if v < self.__valid_min or v > self.__valid_max:
            raise ValueError()
        self._value = v

    @property
    def random_min(self) -> float:
        return self._random_min

    @random_min.setter
    def random_min(self, v: float):
        if v < self.__valid_min or v > self.__valid_max:
            raise ValueError()
        self._random_min = v

    @property
    def random_max(self) -> float:
        return self._random_max

    @random_max.setter
    def random_max(self, v: float):
        if v < self.__valid_min or v > self.__valid_max:
            raise ValueError()
        self._random_max = v

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
        return SensorType.Boolean

    @property
    def value(self) -> bool:
        if self._random:
            return random.choice([True, False])

        return self._value

    @value.setter
    def value(self, v: bool):
        self._value = v

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

class ButtonSensor(BooleanSensorBase):
    def __init__(self, pin):
        super().__init__(pin)

    @staticmethod
    def sensor_name() -> str:
        return 'Button'