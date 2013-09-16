from __future__ import print_function
from random import choice
import sys
#actions = []


def initialise(action_map):
    global actions
    actions = action_map.values()
    print("Initialisation Completed " + str(actions), file=sys.stderr)


def act(state_map):
    #print (actions, file=sys.stderr)
    #print(state_map, file=sys.stderr)
    return choice(actions)

