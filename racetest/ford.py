from racetest.car import CarBase

class Ford(CarBase):

    @property
    def brand(self): return 'Ford'


class Mustang(Ford):

    @property
    def _engine_hp_mean(self): return 310

    @property
    def _engine_hp_std(self): return 10

    @property
    def _engine_n_cylinders(self): return 8

    @property
    def _wheel_diameter_mean(self): return 18

    @property
    def _wheel_diameter_std(self): return 0.5

    @property
    def _wheel_width_mean(self): return 8

    @property
    def _wheel_width_std(self): return 0.25


class Fiesta(Ford):

    @property
    def _engine_hp_mean(self): return 250

    @property
    def _engine_hp_std(self): return 10

    @property
    def _engine_n_cylinders(self): return 4

    @property
    def _wheel_diameter_mean(self): return 16

    @property
    def _wheel_diameter_std(self): return 0.5

    @property
    def _wheel_width_mean(self): return 8

    @property
    def _wheel_width_std(self): return 0.25