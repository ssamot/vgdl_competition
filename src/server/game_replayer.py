from subprocess import Popen, PIPE,check_output
import subprocess
import simplejson as json
from time import sleep
from vgdl.core import VGDLParser
import importlib
import sys
import os
import time
import argparse

def load_game(module_str, level_str, actions):
   
    module  = importlib.import_module(module_str)

    game = None    
    level = None
    
    for key in module.__dict__.keys():
        #print key
        if(key.endswith("game")):
            game = module.__dict__[key]
        if(key.endswith("level") and key == level_str):
            level = module.__dict__[key]
            
    if(level is None):
        return None
    #print game, level
    g = VGDLParser.playGame(game, level, headless = False, persist_movie = False, movie_dir = "./tmp/", actions = actions)
    #g.startGameExternalPlayer(headless = True, persist_movie = True)
    return g


if __name__=="__main__":
    #compile_java("Agent.java")
    #game = load_game("examples.gridphysics.frogs", "frog_level")
    parser = argparse.ArgumentParser(description='Execute an agent vs a list of games and levels.')
    parser.add_argument('--action_file', type=str,
                       help='Temporary directory',required=True)

    args = parser.parse_args()

    with open(args.action_file, "r") as action_file:
        actions = action_file.readline()

    actions = eval(actions)

    print actions
    game = load_game("examples.gridphysics.frogs", "frog_level",actions)