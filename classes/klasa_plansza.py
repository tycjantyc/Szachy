import numpy as np
from enum import Enum
 
class Ruch(Enum):
    BIALY = 1
    CZARNY = -1

class Plansza:

    def __init__(self):
        self.plansza = np.zeros((8,8))
        self.tura = Ruch.BIALY
        self.moves_count = 1

    def stworz_plansze(self):
        self.plansza[7] = np.array([5,2,3,8,4,3,2,5])
        self.plansza[0] = -self.plansza[7]
        self.plansza[6] = np.ones(8)
        self.plansza[1] = -self.plansza[6]
    def zmien_ture(self):
        self.tura = -self.tura          #moze sie tu wysypac ale nie powinno
        if self.tura.equalls(Ruch.BIALY):
            self.moves_count+=1


pl = Plansza()
pl.stworz_plansze()