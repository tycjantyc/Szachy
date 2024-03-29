import numpy as np
from enum import Enum
    
slownik_ruchy = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
slownik_figur = {}


class Kolor(Enum):
    BIALY = 1
    CZARNY = -1

class Figura:
    def __init__(self, polozenie = (0, 0), kolor = Kolor.BIALY):
        self.wartosc = 0
        self.kolor = kolor
        self.polozenie = polozenie
        self.captured = False

    def wykonaj_ruch(self, plansza : np.ndarray, loc_end) -> bool:

        x, y = loc_end
        
        if self.sprawdz_legalnosc_ruchu(plansza, loc_end) and self.kolor.value*plansza[self.polozenie[0], self.polozenie[1]] > 0 and plansza[x, y]*self.kolor.value <= 0:

            plansza[self.polozenie[0], self.polozenie[1]] = 0
            plansza[x, y] = self.wartosc
            self.polozenie = (x, y)

            if type(self) == Pion:
                self.first_move = False

            return True

        else: 
            print("Ruch nielegalny!")
            return False
    
    def sprawdz_legalnosc_ruchu(self, plansza: np.ndarray, loc_end: np.ndarray) -> bool:
        pass

    def wszystkie_legalne_ruchy(self, plansza: np.ndarray) -> list:
        
        lista = []

        for x in range(8):
            for y in range(8):

                loc_end = np.array([x, y])

                if self.sprawdz_legalnosc_ruchu(plansza, loc_end) and self.kolor.value*plansza[self.polozenie[0], self.polozenie[1]] > 0 and plansza[x, y]*self.kolor.value <= 0:
                    lista.append((x, y))
        return lista


class Pion(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        self.kolor = kolor
        self.wartosc = 1*self.kolor.value
        self.polozenie = np.array(polozenie)
        self.captured = False
        self.first_move = True
    
    def wykonaj_ruch(self, plansza: np.ndarray, loc_end):
        
        return super().wykonaj_ruch(plansza, loc_end)
    
    def sprawdz_legalnosc_ruchu(self, plansza : np.ndarray, loc_end) -> bool:

        x, y = self.polozenie
        x1, y1 = loc_end

        if (y == y1 and x - self.kolor.value == x1) and (plansza[x1, y1] == 0):
            return True
        elif ((y == y1 and x - 2*self.kolor.value == x1 and self.first_move) and (plansza[x1, y1] + plansza[x - self.kolor.value , y] == 0)):
            return True
        elif ((y+1 == y1 or y-1 ==y1) and x - self.kolor.value == x1) and plansza[x1, y1] * self.kolor.value < 0:
            return True
        else:
            return False
    
    
        
class Wieza(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        
        self.kolor = kolor
        self.wartosc = 5*self.kolor.value
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(self, plansza: np.ndarray, loc_end):
        return super().wykonaj_ruch(plansza, loc_end)
    

    def sprawdz_legalnosc_ruchu(self,plansza: np.ndarray, komenda_do):
        x1,y1 = komenda_do
        x2,y2 = self.polozenie
        if x1 == x2:
            bool_1 = plansza[x1,y1]*plansza[x2,y2]<=0  #czy figury sa przyciwnych kolorow
            bool_2  = np.all(plansza[x1, min(y1,y2)+1:max(y1,y2)] == 0)
            return np.logical_and(bool_1,bool_2)
        elif y1 == y2:
            
            bool_1 = plansza[x1,y1]*plansza[x2,y2]<=0  #czy figury sa przyciwnych kolorow
            bool_2  = np.all(plansza[min(x1,x2)+1:max(x1,x2), y1] == 0)
            return np.logical_and(bool_1,bool_2)
        else:
            return False

class Kon(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        self.kolor = kolor
        self.wartosc = 2*self.kolor.value
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(self, plansza: np.ndarray, loc_end):
        return super().wykonaj_ruch(plansza, loc_end)
    
    def sprawdz_legalnosc_ruchu(self,plansza: np.ndarray, komenda_do):

        x1,y1 = self.polozenie
        x2,y2 = komenda_do

        if (abs(x2-x1) == 1 and abs(y2-y1) == 2):
            return True
        elif (abs(x2-x1) == 2 and abs(y2-y1) == 1):
            return True
        else:
            return False
        

class Goniec(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        self.wartosc = 3*kolor.value
        self.kolor = kolor
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(self, plansza: np.ndarray, loc_end):
        return super().wykonaj_ruch(plansza, loc_end)
    
    def sprawdz_legalnosc_ruchu(self,plansza: np.ndarray, komenda_do):

        x1,y1 = self.polozenie
        x2,y2 = komenda_do

        if (abs(x2-x1) == abs(y2-y1)): #sprawdzenie poprawności końca
            
            tiles_to_check = [(x, y) for x, y in zip(range(x1, x2, 1 if x2>x1 else -1), range(y1, y2, 1 if y2>y1 else -1))]
            
            if len(tiles_to_check) > 0: 
                tiles_to_check.pop(0)
            values_to_check = [plansza[x, y] for x, y in tiles_to_check]

            if not any(values_to_check):  #i czy jest puste między pozycjami
                return True
            else:
                return False
        else:
            return False
        

class Krolowa(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        
        self.wartosc = 9*kolor.value
        self.kolor = kolor
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(self, plansza: np.ndarray, loc_end):
        return super().wykonaj_ruch(plansza, loc_end)

    def sprawdz_legalnosc_ruchu(self,plansza: np.ndarray, komenda_do):

        fig1 = Wieza(polozenie=self.polozenie, kolor = self.kolor)
        fig2 = Goniec(polozenie=self.polozenie, kolor = self.kolor)
        
        b1 = fig1.sprawdz_legalnosc_ruchu(plansza, komenda_do)
        b2 = fig2.sprawdz_legalnosc_ruchu(plansza, komenda_do)

        return b1 or b2



class Krol(Figura):
    def __init__(self, polozenie, kolor: Kolor):
        
        self.wartosc = 4*kolor.value
        self.kolor = kolor
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(self, plansza: np.ndarray, loc_end):
        return super().wykonaj_ruch(plansza, loc_end)

    def sprawdz_legalnosc_ruchu(self,plansza: np.ndarray, komenda_do):

        x1,y1 = self.polozenie
        x2,y2 = komenda_do

        diff1 = abs(x2-x1)
        diff2 = abs(y2-y1)

        if (diff1 <= 1 and diff2 <= 1) and (diff1 != 0 or diff2 != 0):
            return True
        else:
            return False
