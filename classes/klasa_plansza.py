import numpy as np
from enum import Enum
# from klasy_pionkow import Kolor
# from klasy_pionkow import Pion
# from klasy_pionkow import Wieza
# from klasy_pionkow import Kon
# from klasy_pionkow import Goniec
# from klasy_pionkow import Krol
# from klasy_pionkow import Krolowa

    
slownik_ruchy = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
slownik_figur = {}

class Plansza:

    def __init__(self):

        self.plansza = np.zeros((8,8))
        self.tura = Kolor.BIALY
        self.moves_count = 1
        self.lista_figur = None

    def stworz_plansze(self):

        self.plansza[7] = np.array([5,2,3,8,4,3,2,5])
        self.plansza[0] = -self.plansza[7]
        self.plansza[6] = np.ones(8)
        self.plansza[1] = -self.plansza[6]

    def zmien_ture(self):
     
        if self.tura == Kolor.BIALY:
            self.tura = Kolor.CZARNY
        else:
            self.tura = Kolor.BIALY
            self.moves_count+=1
    
    def stworz_figury(self):

        lista_figur = []
        #pionki
        lista_figur = [Pion((6,i), Kolor.BIALY) for i in range(8)]
        lista_figur += [Pion((1,i), Kolor.CZARNY) for i in range(8)]
        #wieze
        lista_figur += [Wieza((7,i), Kolor.BIALY) for i in [0,7]]
        lista_figur += [Wieza((0,i), Kolor.CZARNY) for i in [0,7]]
        #konie
        lista_figur += [Kon((7,i), Kolor.BIALY) for i in [1,6]]
        lista_figur += [Kon((0,i), Kolor.CZARNY) for i in [1,6]]
        #gońce
        lista_figur += [Goniec((7,i), Kolor.BIALY) for i in [2,5]]
        lista_figur += [Goniec((0,i), Kolor.CZARNY) for i in [2,5]]
        #krolowe
        lista_figur += [Krolowa((7,i), Kolor.BIALY) for i in [3]]
        lista_figur += [Krolowa((0,i), Kolor.CZARNY) for i in [3]]
        #krole
        lista_figur += [Krol((7,i), Kolor.BIALY) for i in [4]]
        lista_figur += [Krol((0,i), Kolor.CZARNY) for i in [4]]

        self.lista_figur = lista_figur
    
def konwersja_komend_do(komenda_do):
        x = slownik_ruchy[komenda_do[0]]
        y = komenda_do[1]
        return (x,y)


def is_legal(komenda):
    x1,y1 = komenda
    return x1>=0 and x1<8 and y1>=0 and y1<8  


class Kolor(Enum):
    BIALY = 1
    CZARNY = -1

class Figura:
    def __init__(self, polozenie = (0, 0), kolor = Kolor.BIALY):
        self.wartosc = 0
        self.kolor = kolor
        self.zakres_ruchu = 1
        self.polozenie = polozenie
        self.captured = False

    def wykonaj_ruch(self, plansza : Plansza, loc_end):

        if self.sprawdz_legalnosc_ruchu(plansza, loc_end):

            plansza.plansza[self.polozenie] = 0
            plansza.plansza[loc_end] = self.wartosc

            self.polozenie = loc_end

        else: 
            print("Ruch nielegalny!")

    # def sprawdz_mozliwosc_ruchu(self, plansza : Plansza, loc_end) -> bool:
        
    #     if plansza.plansza[self.polozenie] * self.kolor > 0 and plansza.plansza[loc_end]:
    #         return True
        
    #     return False
    
    def sprawdz_legalnosc_ruchu(self, plansza: Plansza, loc_end) -> bool:
        pass

class Pion(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        self.wartosc = 1
        self.kolor = kolor
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False
        self.first_move = True

    def set_polozenie(self,x,y):

        self.polozenie = (x, y)
    
    def wykonaj_ruch(self, plansza: Plansza, loc_end):
        self.first_move = False
        return super().wykonaj_ruch(plansza, loc_end)
    
    def sprawdz_legalnosc_ruchu(self, plansza : Plansza, loc_end) -> bool:

        x, y = self.polozenie
        x1, y1 = loc_end

        if (x == x1 and y + self.kolor.value == y1) and (plansza.plansza[loc_end] != 0):
            return True
        elif ((x == x1 and y + 2*self.kolor.value == y1 and self.first_move) and (plansza.plansza[loc_end] + plansza.plansza[(x, y + self.kolor.value)] == 0)):
            return True
        elif ((x+1 == x1 or x-1 ==x1) and y + self.kolor == y1) and plansza.plansza[loc_end] * self.kolor < 0:
            return True
        else:
            return False
        
        
        

class Wieza(Figura):
    def __init__(self, polozenie, kolor):
        self.wartosc = 1
        self.kolor = Kolor.BIALY
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(komenda):
        pass
    def set_polozenie(self,x,y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def sprawdz_mozliwosc_ruchu(self,plansza, komenda_do):
        x1,y1 = komenda_do
        x2,y2 = self.polozenie
        if x1.equals(x2):
            bool_1 = plansza[komenda_do]*plansza[self.polozenie]<=0  #czy figury sa przyciwnych kolorow
            bool_2  = np.all(plansza[x1, min(y1,y2)+1:max(y1,y2)] == 0)
            return np.logical_and(bool_1,bool_2)
        elif y1.equals(y2):
            
            bool_1 = plansza[komenda_do]*plansza[self.polozenie]<0  #czy figury sa przyciwnych kolorow
            bool_2  = np.all(plansza[min(x1,x2)+1:max(x1,x2), y1] == 0)
            return np.logical_and(bool_1,bool_2)
        else:
            return False

class Kon(Figura):
    def __init__(self, polozenie, kolor):
        self.wartosc = 1
        self.kolor = Kolor.BIALY
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(komenda):
        pass
    def set_polozenie(self,x,y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def sprawdz_mozliwosc_ruchu(plansza):
        pass

class Goniec(Figura):
    def __init__(self, polozenie, kolor):
        self.wartosc = 1
        self.kolor = Kolor.BIALY
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(komenda):
        pass
    def set_polozenie(self,x,y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def sprawdz_mozliwosc_ruchu(self,plansza,komenda_do):
        if abs(komenda_do[0]-self.polozenie[0]).equals(komenda_do[1]-self.polozenie[1]): 
            return True
        else:
            return False

class Krolowa(Figura):
    def __init__(self, polozenie, kolor):
        self.wartosc = 1
        self.kolor = Kolor.BIALY
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(komenda):
        pass
    def set_polozenie(self,x,y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def sprawdz_mozliwosc_ruchu(plansza):
        pass

class Krol(Figura):
    def __init__(self, polozenie, kolor):
        self.wartosc = 1
        self.kolor = Kolor.BIALY
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(komenda):
        pass
    def set_polozenie(self,x,y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def sprawdz_mozliwosc_ruchu(plansza):
        pass
