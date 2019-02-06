import abc

import numpy as np


class CarBase(abc.ABC):

    N_WHEELS = 4

    def __init__(self, random_seed):
        np.random.seed(random_seed)
        self.engine = self.get_engine()
        self.wheels = [self.get_wheel() for _ in range(self.N_WHEELS)]

    @property
    @abc.abstractmethod
    def brand(self): pass

    @property
    def model(self): return self.__class__.__name__

    @property
    @abc.abstractmethod
    def _engine_hp_mean(self): return 300

    @property
    @abc.abstractmethod
    def _engine_hp_std(self): return 10

    @property
    @abc.abstractmethod
    def _engine_n_cylinders(self): return 8

    @property
    @abc.abstractmethod
    def _wheel_diameter_mean(self): return 18

    @property
    @abc.abstractmethod
    def _wheel_diameter_std(self): return 0.5

    @property
    @abc.abstractmethod
    def _wheel_width_mean(self): return 8

    @property
    @abc.abstractmethod
    def _wheel_width_std(self): return 0.25

    def get_engine(self):
        return Engine(
            self._engine_n_cylinders, 
            np.random.normal(self._engine_hp_mean, self._engine_hp_std))

    def get_wheel(self):
        return Wheel(
            np.random.normal(self._wheel_diameter_mean, self._wheel_diameter_std),
            np.random.normal(self._wheel_width_mean, self._wheel_width_std))


class Wheel:

    def __init__(self, diameter, width):
        self.diameter = diameter
        self.width = width


class Engine:

    def __init__(self, n_cylinders, horsepower):
        self.n_cylinders = n_cylinders
        self.horsepower = horsepower
