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
from random import randint
import ntpath






supported_file_names = {}
supported_file_names["python"] = "agent.py"
supported_file_names["Java"] = "Agent.java"
supported_file_names["C"] = "agent.c"

supported_languages = {v:k for k, v in supported_file_names.items()}




def execute_python(dir_name, args, game):
    return randint(1,10)

def clean_exit(dir_name,clean):
    print clean
    if(clean):
        if(os.path.isdir(dir_name)):
            shutil.rmtree(dir_name)
    exit(0)

def detect_language(dir_name):
    root_files = glob.glob(dir_name + "/*")

    for root_file in root_files:
        file_name  = ntpath.basename(root_file)
        if file_name in supported_languages:
            return supported_languages[file_name]
            
    return None

def main(args):
   
    #print args.tmp_dir, args.user_name, args.run_id
    dir_name = args.tmp_dir + "/" + args.user_name +  "/" + str(args.run_id)     

        
    if(os.path.isdir(dir_name)):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)   
   
    logger = logging.getLogger('game_executor')
    hdlr = logging.FileHandler(dir_name + '/execution.log')
    #print dir_name + '/execution.log'
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)

   
    
    logger.debug("zip_name " + str(args.zip_name))
    logger.debug("run_id " +  str(args.run_id))
    logger.debug("user_id "  + str(args.agent_id))
    try:
        with zipfile.ZipFile(args.zip_name, "r") as z:
            z.extractall(dir_name)
	
	shutil.copy(args.zip_name, dir_name)


    except Exception, e: # Catch all possible exceptions 
        logger.critical("Cannot extract zip archive, " + str(e))
        clean_exit(dir_name, args.clean)
    
    language = detect_language(dir_name)
    if(language == None):
        logger.critical("Language not supported")
        clean_exit(dir_name, args.clean)
        
        
    exec_function = None
    if(language == "python"):
        exec_function = execute_python
        
    
    scores = [exec_function(dir_name, args, game)for game in args.game_ids for i in range(args.n_times)]
    action_file_names = [i for i in range(len(scores))]    
    print scores, action_file_names
    logger.info(str(scores)[1:-1])
    logger.info(str(action_file_names)[1:-1])    

    
    if(args.clean):
        clean_exit(dir_name, args.clean)
    
if __name__=="__main__":
    # List of games
    # Number of times game is to be executed
    # Zip file name
    # agent ID
    # Run ID
    parser = argparse.ArgumentParser(description='Execute an agent vs a list of games.')
    parser.add_argument('--game_ids', type=int, nargs='+',
                       help='List of game ids to execute',required=True)
    parser.add_argument('--n_times', type=int,
                       help='Number of times to run each game',required=True)  
    parser.add_argument('--zip_name', type=str,
                       help='Zip file name of agent',required=True)  
    parser.add_argument('--agent_id', type=int,
                       help='Id of the agent',required=True)  
    parser.add_argument('--run_id', type=int,
                       help='Id of the current run',required=True)              
    parser.add_argument('--user_name', type=str,
                       help='User name of the player',required=True)  
    parser.add_argument('--tmp_dir', type=str,
                       help='Temporary directory',required=True)
    parser.add_argument('--clean', type=bool,
                       help='Should I clean-up after running this',required=True)  
                       
                       
    args = parser.parse_args()
    main(args) 
    


