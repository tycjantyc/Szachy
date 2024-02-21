from figury import *
import numpy as np

class Game:

    def __init__(self, plansza = np.zeros((8,8)), lista_figur = None):

        self.plansza = plansza
        self.tura = Kolor.BIALY
        self.moves_count = 1
        self.action_size = 64
        self.lista_figur = lista_figur
        self.white_won = False
        self.black_won = False

        self.stworz_plansze()
        self.stworz_figury()

    def stworz_plansze(self):

        self.plansza[7] = np.array([5,2,3,9,4,3,2,5])
        self.plansza[0] = -self.plansza[7]
        self.plansza[6] = np.ones(8)
        self.plansza[1] = -self.plansza[6]

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

    def zmien_ture(self):
     
        if self.tura == Kolor.BIALY:
            self.tura = Kolor.CZARNY
        else:
            self.tura = Kolor.BIALY
            self.moves_count+=1
    
    def get_value_and_terminated(self, state = None, action = None) -> tuple[int, bool]:
        
        if action is not None:
            p1, p2 = action
            
            state[p2[0], p2[1]] = state[p1[0], p1[1]]
            state[p1[0], p1[1]] = 0
            
        if state is None and action is None:
            state = self.plansza

        state = state.flatten()
        state = state[abs(state) == 4]

        if len(state) == 1 and state[0] == 4:
            1, True
        elif len(state) == 1 and state[0] == -4:
            -1, True
        else:
            return 0, False
    
    def get_valid_moves(self) -> list:
        
        lista_ruchow = []

        for fig in self.lista_figur:
            if fig.kolor.value == self.tura.value:
                lista_ruchow.append(fig.wszystkie_legalne_ruchy(self.plansza))

        return lista_ruchow
    

    def get_valid_moves(self, state: np.ndarray) -> list:

        lista_fig = []

        for i in range(8):
            for j in range(8):
                kolor = None
                if state[i, j] > 0:
                    kolor = Kolor.BIALY
                else:
                    kolor = Kolor.CZARNY

                if abs(state[i, j]) == 1:
                    lista_fig.append(Pion((i, j), kolor))
                elif abs(state[i, j]) == 2:
                    lista_fig.append(Kon((i, j), kolor))
                elif abs(state[i, j]) == 3:
                    lista_fig.append(Goniec((i, j), kolor))
                elif abs(state[i, j]) == 5:
                    lista_fig.append(Wieza((i, j), kolor))
                elif abs(state[i, j]) == 4:
                    lista_fig.append(Krol((i, j), kolor))
                elif abs(state[i, j]) == 9:
                    lista_fig.append(Krolowa((i, j), kolor))
                
        lista_ruchow = []

        for fig in lista_fig:
            if fig.kolor.value == 1:
                ruchy = fig.wszystkie_legalne_ruchy(state)
                
                for ruch in ruchy:
                    lista_ruchow.append([fig.polozenie, ruch])
                
        return lista_ruchow

    def get_current_state(self):

        return self.plansza
    
    def change_perspective(self, state, player : Kolor):

        return state * player.value
    
    def make_move(self, ruch):
        
        for fig in self.lista_figur:
            if fig.polozenie[0] == ruch[0][0] and fig.polozenie[1] == ruch[0][1]:
                print("ok!!!!!!!")
                fig.wykonaj_ruch(self.plansza, ruch[1])
                break

    def get_opponent(self, player: Kolor):
        
        if player.value > 0:    
            return Kolor.CZARNY
        
        return Kolor.BIALY
    
    def get_opponent_value(self, value:int):
        
        return -value
    
    def get_next_state(self, state, action, val = 1):

        print("Action:" + str(action))
        p1, p2 = action

        state[p2[0], p2[1]] = state[p1[0], p1[1]]
        state[p1[0], p1[1]] = 0

        return state


    
    def play_2_people(self):

        while(True):
            
            print("Ruch koloru " + "białego" if self.tura.value > 0 else "czarnego")
            print(self.plansza)

            flag = False
    
            while(not flag):
                print("Wpisz koordynaty figury")
                wybor_figury = input()
                wybor_figury = np.array([int(i) for i in wybor_figury.split(" ")])
                
                figura = Figura()

                for fig in self.lista_figur:
                    
                    if all(fig.polozenie == wybor_figury):
                        figura = fig
                        break
                print("Możliwe ruchy:")
                print(figura.wszystkie_legalne_ruchy(self.plansza))

                print("Wpisz koordynaty nowego położenia figury")
                ruch = input()
                ruch = np.array([int(i) for i in ruch.split(" ")])

                

                flag = figura.wykonaj_ruch(self.plansza, ruch)

            if self.sprawdz_czy_koniec():
                break

            self.zmien_ture()

        if self.black_won:
            print("Black WON!")
        else:
            print("White WON!")


#game = Game()
#game.play_2_people()