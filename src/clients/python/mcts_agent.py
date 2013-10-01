from __future__ import print_function
from random import choice
import sys
import simplejson as json
import random
from client import queryStateActionJSON, queryStateAction
from UCT import UCT
#actions = []


class SimpleGameState:
    """ A state of the game Nim. In Nim, players alternately take 1,2 or 3 chips with the
        winner being the player to take the last chip.
        In Nim any initial state of the form 4n+k for k = 1,2,3 is a win for player 1
        (by choosing k) chips.
        Any initial state of the form 4n is a win for player 2.
    """
    def __init__(self, state_str, moves,depth):
        self.playerJustMoved = 1 # At the root pretend the player just moved is p2 - p1 has the first move
        self.moves = moves
        self.state = state_str
        self.map_state = json.loads(self.state)
        self.depth = 0
    def Clone(self):
        """ Create a deep clone of this game state.
        """
        st = SimpleGameState(self.state, self.moves, self.depth)
        st.playerJustMoved = 1
        return st

    def DoMove(self, move):
        """ Update a state by carrying out the given move.
            Must update playerJustMoved.
        """
        #print (self.state+ str(move), file=sys.stderr)
        self.state = queryStateAction(self.state,move)
        self.map_state = json.loads(self.state)
        #print ("pongo" + str(move), file=sys.stderr)
        self.playerJustMoved = 1
        self.depth+=1

    def GetMoves(self):
        """ Get all possible moves from this state.
        """
        #print (self.moves, file=sys.stderr)
        #print ("score" + str(self.map_state["score"]) + "----" + str(self.depth), file=sys.stderr)
        score = self.map_state["score"]
        if(score == 1001 or score == 0   or self.depth > 30):
            #print ("finished_run" + str(score), file=sys.stderr)

            return []
        return self.moves[:]

    def GetResult(self, playerjm):
        """ Get the game result from the viewpoint of playerjm.
        """
        return self.map_state["score"]

    #def __repr__(self):







def initialise(action_map):
    global actions
    actions = action_map.values()
    print("Initialisation Completed " + str(actions), file=sys.stderr)


def act(state_map):
    #print (actions, file=sys.stderr)
    #print(state_map, file=sys.stderr)
    #print ("Actions" , str(actions), file=sys.stderr)
    state_str = json.dumps(state_map)

    state = SimpleGameState(state_str,actions[:],0)
    m = UCT(rootstate = state, itermax = 100, verbose = False)
    print ("Chosen move" , str(m), file=sys.stderr)
    return m
    #return choice(actions)
    #return actions[0]

#def act(state_map):
#    #print (actions, file=sys.stderr)
#    #print(state_map, file=sys.stderr)
#    action = choice(actions)
#    state_str = json.dumps(state_map)
#    value = state_map["score"]
#    #print (value, file=sys.stderr)
#    state_map["score"] = 0
#    for i in range(100):
#        ts = queryStateAction(state_str,action)
#
#
#    return choice(actions)


