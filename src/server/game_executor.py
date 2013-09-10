# -*- coding: utf-8 -*-
"""
Main File for running games
"""

import argparse 
from progressbar import Bar, ETA,  Percentage, ProgressBar
import zipfile
import glob
import logging
import os
import shutil
import subprocess





supported_file_names = {}
supported_file_names["python"] = "agent.py"
supported_file_names["Java"] = "Agent.java"
supported_file_names["C"] = "agent.c"

supported_languages = {v:k for k, v in supported_file_names.items()}


TMP_DIR_NAME = "/tmp"

def execute_python(dir_name, args, game):
    return 5

def clean_exit(clean):
    if(clean):

def detect_language(dir_name):
    root_files = glob.glob(dir_name)
    for root_file in root_files:
        if root_file in supported_languages:
            return supported_languages[root_file]
            
    return None

def main(args):
    
    logger = logging.getLogger('game_executor')
    hdlr = logging.FileHandler(args.run_id + '.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.WARNING)


    dir_name = TMP_DIR_NAME + "/" +  args.run_id     

        
    
    shutil.rmtree(dir_name)
    os.makedirs(dir_name)

    with zipfile.ZipFile(args.zip_name, "r") as z:
        z.extractall(dir_name)
    
    language = detect_language(dir_name)
    if(language == None):
        logger.error("Language Not Supported")
        clean_exit()
        
        
    exec_function = None
    if(language == "python"):
        exec_function = execute_python
        
    
    [exec_function(dir_name, args, game)for game in args.game_ids for i in range(args.n_times)]
        
    # clean up
        

    
if __name__=="__main__":
    # List of games
    # Number of times game is to be executed
    # Zip file name
    # agent ID
    # Run ID
    parser = argparse.ArgumentParser(description='Execute an agent vs a list of games.')
    parser.add_argument('--game_ids', type=int, nargs='+',
                       help='List of game ids to execute',required=True)
    parser.add_argument('--n_times', type=int, nargs=1,
                       help='Number of times to run each game',required=True)  
    parser.add_argument('--zip_name', type=str, nargs=1,
                       help='Zip file name of agent',required=True)  
    parser.add_argument('--agent_id', type=int, nargs=1,
                       help='Id of the agent',required=True)  
    parser.add_argument('--run_id', type=int, nargs=1,
                       help='Id of the current run',required=True)  
    parser.add_argument('--clean', type=bool, nargs=1,
                       help='Should I clean-up after running this',required=True)  
                       
                       
    args = parser.parse_args()
    main(args) 
    


