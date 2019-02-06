from racetest.ford import Mustang, Fiesta
from racetest.subaru import WRX, Liberty

class Race:

    def __init__(self, random_seed):
        self.name = f'Race #{random_seed}'
        self.mustangs  = [Mustang(random_seed) for _ in range(2)]
        self.fiestas   = [Fiesta(random_seed)  for _ in range(2)]
        self.wrxs      = [WRX(random_seed)     for _ in range(2)]
        self.liberties = [Liberty(random_seed) for _ in range(2)]
