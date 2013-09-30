from __future__ import print_function
from random import choice
import sys
import simplejson as json
import random
from client import queryStateActionJSON, queryStateAction
#actions = []

def add_value(state, action, value):
    if(state in total):
        total[(state,action)]+=value
        visits[(state,action)]+=1
    else:
        total[(state,action)] = value
        visits[(state,action)] = 1

def get_value(state, action, value):
    if(state in total):
        val = total[(state,action)]
        iter = visits[(state,action)]
        return val/float(iter)
    else:
        return 99999+random.random()


def initialise(action_map):
    global actions
    global total
    global visits
    total = {}
    visits = {}
    actions = action_map.values()
    print("Initialisation Completed " + str(actions), file=sys.stderr)


def act(state_map):
    #print (actions, file=sys.stderr)
    #print(state_map, file=sys.stderr)
    action = choice(actions)
    state_str = json.dumps(state_map)
    value = state_map["score"]
    print (value, file=sys.stderr)
    state_map["score"] = 0
    for i in range(100):
        ts = queryStateAction(state_str,action)
    #print(ts, file=sys.stderr)
    add_value(state_str,action,value)

    return choice(actions)


