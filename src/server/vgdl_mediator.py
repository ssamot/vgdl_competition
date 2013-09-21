from subprocess import Popen, PIPE,check_output
import subprocess
import simplejson as json
from time import sleep
from vgdl.core import VGDLParser
import importlib
import sys
import os


DUMMY_COMMAND = {}
DUMMY_COMMAND["Dummy"] = 1
DUMMY_COMMAND["Dummy"] = 2

END_COMMAND = "END_COMMAND\n"

MAXIMUM_TICKS = 1000


def mediate(game, args,headless = True, persist_movie = True):
    p = Popen(args, shell=True, bufsize=1000000,
          stdin=PIPE, stdout=PIPE, close_fds=True)

    actions = game.getPossibleActions()
    j_actions = json.dumps(actions)
    
    # Initialise the player by passing all possible actions
    p.stdin.write(j_actions + os.linesep);p.stdin.flush()
    line = p.stdout.readline()
    
    
    win = None
    score = 0     
    error = None
    # play until game ends
    actions = []
    ticks = 0
    while win is None and ticks< 1000: 
        print ticks
        ticks+=1
        state = game.getFullState()
        j = json.dumps(state)
        
        p.stdin.write(j + os.linesep);p.stdin.flush()
        
        line = p.stdout.readline()
        j_action = json.loads(line)
      
        action = j_action["action"]  
        actions.append(action)
        win,score = game.tick(action,headless, headless)
        #exit(0)
    if(score is None):
        score = 0
    return win,score, actions, error
def load_game(module_str, level_str):
   
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
    g = VGDLParser.playGame(game, level, headless = True, persist_movie = True, movie_dir = "./tmp/")
    #g.startGameExternalPlayer(headless = True, persist_movie = True)
    return g

def compile_java(file_name):
    p = Popen("javac " + file_name, shell=True, bufsize=1000000,
          stderr=PIPE, stdout=PIPE, close_fds=True)
          
    out, err = p.communicate()
    print out
    print err

if __name__=="__main__":
    #compile_java("Agent.java")
    game = load_game("examples.gridphysics.frogs")
    print mediate(game,"python /home/ssamot/projects/vgdl/vgdl_competition/src/clients/python/client.py")
    #args = ["java", "-cp" ]
    #grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
    #p.communicate()
    
            
            
        
        
          
         
   
     