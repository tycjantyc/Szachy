import numpy as np
from klasa_plansza import Plansza
from enum import Enum



class Kolor(Enum):
    BIALY = 1
    CZARNY = -1

class Figura:
    def __init__(self):
        self.wartosc = 0
        self.kolor = Kolor.BIALY
        self.zakres_ruchu = 1
        self.polozenie = np.zeros(2)
        self.captured = False

    def wykonaj_ruch():
        pass

    def sprawdz_mozliwosc_ruchu(plansza):
        pass

class Pion(Figura):
    def __init__(self, polozenie, kolor):
        self.wartosc = 1
        self.kolor = kolor
        self.zakres_ruchu = 1
        self.polozenie = np.array(polozenie)
        self.captured = False

    def wykonaj_ruch(komenda):
        pass
    def set_polozenie(self,x,y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def sprawdz_mozliwosc_ruchu(self,plansza, komenda_do):
        #funkcja powinna dzialac
        poz1 = (self.polozenie[0]+1, self.polozenie[1]+1*self.kolor)
        poz2 = (self.polozenie[0]-1, self.polozenie[1]+1*self.kolor)
        poz3 = (self.polozenie[0], self.polozenie[1]+1*self.kolor)
        opcje = [poz1,poz2,poz3]
        if komenda_do.equals(poz1) and self.kolor*plansza[poz1] < 0 or komenda_do.equals(poz2) and self.kolor*plansza[poz2] < 0:
            return True
        elif komenda_do.equals(poz3) and plansza[poz3].equals(0):
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



def main():
    plansza = klasa_plansza.Plansza()
    plansza.stworz_plansze()
    plansza.stworz_figury()
    figura = [i for i in plansza.lista_figur if i.polozenie.equals(0,0)]
    
    print("chuj")
main()