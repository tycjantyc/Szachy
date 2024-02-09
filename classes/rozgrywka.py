from klasa_plansza import *
import numpy as np

def play():

    plansza = Plansza()
    plansza.stworz_plansze()
    plansza.stworz_figury()

    while(True):
        
        print("Ruch koloru " + "białego" if plansza.tura.value > 0 else "czarnego")
        print(plansza.plansza)

        print("Wpisz koordynaty figury")
        wybor_figury = input()
        wybor_figury = np.array([int(i) for i in wybor_figury.split(" ")])
        
        print("Wpisz koordynaty nowego położenia figury")
        ruch = input()
        ruch = np.array([int(i) for i in ruch.split(" ")])

        figura = Figura()

        for fig in plansza.lista_figur:
            print(fig.polozenie)
            print(wybor_figury)
            if all(fig.polozenie == wybor_figury):
                figura = fig
                break

    
    
        figura.wykonaj_ruch(plansza, ruch)

        plansza.zmien_ture()

    
play()