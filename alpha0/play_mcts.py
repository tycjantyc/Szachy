from mcts import *

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "c:\\Users\\Jan\\Desktop\\Szachy")
sys.path.insert(1, "c:\\Users\\Jan\\Desktop\\Szachy\\classes")

from classes.rozgrywka import *

chess = Game()

player = Kolor.BIALY

args = {
    'C': 1.41,
    'num_searches': 1000
}

mcts = MCTS(chess, args)

state = chess.get_current_state()


while True:

    print(state)
    
    valid_moves = chess.get_valid_moves(state)
    
    if player.value == 1:
        
        print("valid_moves", [i for i in valid_moves])
        action = int(input(f"{player}:"))
    
    else:
        neutral_state = chess.change_perspective(state, player)
        mcts_probs = mcts.search(neutral_state)
        action = np.argmax(mcts_probs)

    chess.make_move(valid_moves[action])    
    state = chess.get_current_state()

    value, is_terminal = chess.get_value_and_terminated()
    
    if is_terminal:
        print(state)
        
    player = chess.get_opponent(player)