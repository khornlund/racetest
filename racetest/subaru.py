from racetest.car import CarBase

class Subaru(CarBase):

    @property
    def brand(self): return 'Subaru'


class WRX(Subaru):

    @property
    def _engine_hp_mean(self): return 305

    @property
    def _engine_hp_std(self): return 5

    @property
    def _engine_n_cylinders(self): return 4

    @property
    def _wheel_diameter_mean(self): return 16

    @property
    def _wheel_diameter_std(self): return 0.5

    @property
    def _wheel_width_mean(self): return 9

    @property
    def _wheel_width_std(self): return 0.3


class Liberty(Subaru):

    @property
    def _engine_hp_mean(self): return 175

    @property
    def _engine_hp_std(self): return 5

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