from __future__ import print_function
from random import choice
import sys
import simplejson as json
import random
from client import queryStateActionJSON, queryStateAction
from UCT import UCT
import math
import numpy as np
#actions = []

def printe(*args):
    print (*args  , file=sys.stderr)


class SimpleGameState:
    """ A state of the game Nim. In Nim, players alternately take 1,2 or 3 chips with the
        winner being the player to take the last chip.
        In Nim any initial state of the form 4n+k for k = 1,2,3 is a win for player 1
        (by choosing k) chips.
        Any initial state of the form 4n is a win for player 2.
    """
    def __init__(self, state_str, moves,depth, score):
        self.playerJustMoved = 1 # At the root pretend the player just moved is p2 - p1 has the first move
        self.moves = moves
        self.state = state_str
        self.map_state = json.loads(self.state)
        self.depth = 0
        self.score = score
        self.gamma = 0.98
    def Clone(self):
        """ Create a deep clone of this game state.
        """
        st = SimpleGameState(self.state, self.moves, self.depth, self.score)
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
        avatar = self.map_state["objects"]["avatar"]
        goal = self.map_state["objects"]["goal"]
        if(not self.ended()):
            #print (avatar , file=sys.stderr)
            goal_position = eval(self.map_state["objects"]["goal"].keys()[0])
            avatar_position = eval(self.map_state["objects"]["avatar"].keys()[0])
            #score = 0
            score = -self.dist(goal_position, avatar_position)/1000.0
            #print (goal_position,avatar_position , file=sys.stderr)
        else:
            score = self.map_state["score"]
        #else:
        #    score = -1
        #printe(self.score)
        self.score += score * self.gamma
        #printe(self.score)
    def GetMoves(self):
        """ Get all possible moves from this state.
        """
        #printe(self.moves[:])
        if(self.map_state["ended"] or self.depth > 5):
            #print ("finished_run" + str(score), file=sys.stderr)

            return []
        return self.moves[:]

    def GetResult(self, playerjm):
        """ Get the game result from the viewpoint of playerjm.
        """
        return self.score


    def ended(self):
        avatar = self.map_state["objects"]["avatar"]
        return self.map_state["ended"] or len(avatar.keys()) == 0

    def dist(self, p1,p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 +
                     (p2[1] - p1[1]) ** 2 )
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

    state = SimpleGameState(state_str,actions[:],0,0)
    #print ("Chosen move" , str(state_str), file=sys.stderr)
    m = UCT(rootstate = state, itermax = 100, verbose = False)
    #print ("Chosen move" , str(m), file=sys.stderr)
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


