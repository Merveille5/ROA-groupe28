import numpy as np
from collections import defaultdict
import math
import random

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

# ***************************
# JEU MORPION
# INITIALISATION DU PROGRAMME 
# ****************************
def initial_state():
    return [EMPTY] * 9

def get_moves(state):
    return [i for i in range(9) if state[i] == EMPTY]

def play_move(state, move, player):
    new_state = state.copy()
    new_state[move] = player
    return new_state

def switch_player(player):
    return PLAYER_O if player == PLAYER_X else PLAYER_X

def check_winner(state):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in wins:
        if state[a] == state[b] == state[c] and state[a] != EMPTY:
            return state[a]
    return None

def is_terminal(state):
    return check_winner(state) or EMPTY not in state

def result(state, player):
    winner = check_winner(state)
    if winner == player:
        return 1
    elif winner is None:
        return 0
    else:
        return -1


# ***************************************
# HEURISTIQUE / OPTIMISATION DU PROGRAMME 
# ***************************************
def smart_move(state, player):
    moves = get_moves(state)

    # cas 1. Gagner immédiatement
    for m in moves:
        if check_winner(play_move(state, m, player)) == player:
            return m

    # cas 2. Bloquer l’adversaire
    opponent = switch_player(player)
    for m in moves:
        if check_winner(play_move(state, m, opponent)) == opponent:
            return m

    # cas 3. Centre
    if 4 in moves:
        return 4

    # cas 4. Coins
    for m in [0,2,6,8]:
        if m in moves:
            return m

    # cas 5. Sinon aléatoire
    return random.choice(moves)


# *************************
# IMPLEMENTATION CLASSE NODE 
# **************************
class Node:
    def __init__(self, state, player, parent=None):
        self.state = state
        self.player = player
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0

    def is_fully_expanded(self):
        return len(self.children) == len(get_moves(self.state))


# *************
# SELECTION UCT
# *************
def uct(node, total_visits, c=1.41):
    if node.visits == 0:
        return float("inf")
    return (node.wins / node.visits) + c * math.sqrt(math.log(total_visits) / node.visits)


# *****
# MCTS
# *****
def select(node):
    while node.children:
        node = max(node.children, key=lambda n: uct(n, node.visits))
    return node

def expand(node):
    tried_states = [child.state for child in node.children]

    for move in get_moves(node.state):
        new_state = play_move(node.state, move, node.player)
        if new_state not in tried_states:
            next_player = switch_player(node.player)
            child = Node(new_state, next_player, node)
            node.children.append(child)
            return child

    return node

def simulate(state, player):
    current_player = player

    while not is_terminal(state):
        move = smart_move(state, current_player)  
        state = play_move(state, move, current_player)
        current_player = switch_player(current_player)

    return result(state, player)

def backpropagate(node, res):
    while node:
        node.visits += 1
        node.wins += res
        res = -res
        node = node.parent


def mcts(root_state, player, iterations=2000):
    root = Node(root_state, player)

    for _ in range(iterations):
        node = select(root)

        if not is_terminal(node.state):
            node = expand(node)

        res = simulate(node.state, node.player)
        backpropagate(node, res)

    # choisir le meilleur coup
    best_child = max(root.children, key=lambda n: n.visits)
    return best_child.state


# **********************
# AFFICHAGE DU PROGRAMME
# **********************
def print_board(state):
    print("\n")
    print(f" {state[0]} | {state[1]} | {state[2]}")
    print("---+---+---")
    print(f" {state[3]} | {state[4]} | {state[5]}")
    print("---+---+---")
    print(f" {state[6]} | {state[7]} | {state[8]}")
    print("\n")

# ****************
# TEST ET ANALYSE
# *****************
if __name__ == "__main__":
    print(" Que la partie commence !")
    print("Tu es le joueur X et l'IA est O")
    print("Les positions vont de 0 à 8 :")
    
    print("""
     0 | 1 | 2
    ---+---+---
     3 | 4 | 5
    ---+---+---
     6 | 7 | 8
    """)

    state = initial_state()
    player = PLAYER_X

    print(" La partie commence !\n")
    while not is_terminal(state):

        print_board(state)

        if player == PLAYER_X:
            # Joueur humain
            try:
                move = int(input(" Ton coup (0-8) : "))
                if move not in get_moves(state):
                    print(" Case invalide, réessaie.")
                    continue
            except:
                print(" Entrée invalide.")
                continue

        else:
            # IA joue
            print(" L'IA réfléchit...")
            state = mcts(state, player, iterations=2000)
            player = switch_player(player)
            continue

        # appliquer le coup du joueur
        state = play_move(state, move, player)
        player = switch_player(player)

    # Fin de partie
    print_board(state)
    winner = check_winner(state)

    print("Fin de la partie !")

    if winner == PLAYER_X:
        print(" Bravo ! Tu as gagné !")
    elif winner == PLAYER_O:
        print(" L'IA a gagné !")
    else:
        print(" Match nul !")

        #FIN DU PROGRAMME 
