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
from vgdl_mediator import load_game, mediate
import db_utils
import results_manager







supported_file_names = {}
supported_file_names["python"] = "client.py"
supported_file_names["Java"] = "Client.java"
supported_file_names["C"] = "client.c"


execution_commands = {}
execution_commands["python"] = "cd {dir_name}; python client.py"


supported_languages = {v:k for k, v in supported_file_names.items()}


def tuple_to_str(tpl):
    #print  (",".join(map(str,tpl)))[:-1], tpl
    return "(" + ",".join(map(str,tpl)) + ")"


def extract_game_map(args):
    game_levels = args.game_levels.split(":")
    game_map = {}
    db = None
    for game_level in game_levels:
        levels = game_level.split(",")
        game = levels[0]
        lvls = levels[1:]
        if(game.isdigit()):
            if(db is None):
                db = db_utils.db_connect(args.db_properties)
            #print db_utils.get_game_info(db,game)
            game_name = (long(game), db_utils.get_game_info(db,game)["game_desc_file"])
            #print db_utils.get_levels_from_game(db,game)
            lvl_rows = db_utils.get_levels_from_game(db,game)
            lvl_map= {str(row[0]): row[1] for row in lvl_rows}
           # lvl_ids   =  [str(row[0]) for row in lvl_rows ]
            #lvl_names = 
            #print lvl_rows
            lvl_names = []   
            for row in lvls:
                #print row, lvls,lvl_rows
                if(str(row) in lvl_map.keys()):
                    lvl_names.append((long(row),lvl_map[str(row)]))
            
            #lvls =  [(long(row[0]),row[1]) if row[0] in lvls for row in lvl_rows]
            #print lvls, exit(0) 
            #print game_name, lvl_names
            game_map[game_name] = tuple(lvl_names)
            
        else:
            lvl_names = zip(tuple(range(0,len(lvls))), lvls)
            #print lvl_names
            game_map[(-100L,game)] = tuple(lvl_names)
            
    return game_map
    
def execute_game_map(logger, game_map, args, cmd_line, dir_name,execution_log):
    for module in game_map:
        for level in game_map[module]:
            print level
            game = load_game(module[1],level[1])
            if(game == None):
                logger.fatal(tuple_to_str(module) + ", " + tuple_to_str(level)  + ", "  +  "Cannot Load game/level")
                clean_exit(args, logger, dir_name, execution_log)
            win, score, actions, error_str  = mediate(game,cmd_line)
            action_filename = dir_name + "/" + str(module[1]) + "_" + str(level[1]) + "_actions.log"
            with open(action_filename, "w") as action_file:
                action_file.write(str(actions))
            if(error_str is None):
                logger.info(tuple_to_str(module) + " " + tuple_to_str(level) + " "  +  str(score) + " "  +  str(action_filename))
            else: 
                logger.error(tuple_to_str(module) + " " + tuple_to_str(level)  + " "  + error_str)
                clean_exit(args, logger, dir_name, execution_log)
            


def clean_exit(args, logger, dir_name,execution_log):
    if(args.upload):
        args.execution_log = execution_log
        print "Uploading results to DB"
        results_manager.process_log(args)
    if(args.clean):
        if(os.path.isdir(dir_name)):
            shutil.rmtree(dir_name)
    logger.debug("RUN_COMPLETED")
    exit(0)

def detect_language(dir_name):
    root_files = glob.glob(dir_name + "/*")

    for root_file in root_files:
        file_name  = ntpath.basename(root_file)
        if file_name in supported_languages:
            return supported_languages[file_name]
            
    return None
    


def explode_run(args):
   
    #print args.tmp_dir, args.user_name, args.run_id
    dir_name = args.tmp_dir + "/" + args.user_name +  "/" + str(args.run_id)     

        
    if(os.path.isdir(dir_name)):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)   
    
    # copy file names here
    shutil.copy(args.zip_name, dir_name)

    logger = logging.getLogger('game_executor')
    execution_log = dir_name + '/execution.log'
    hdlr = logging.FileHandler(execution_log)
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
	
    except Exception, e: # Catch all possible exceptions 
        logger.critical("Cannot extract zip archive, " + str(e))
        clean_exit(args, logger, dir_name, execution_log)
    
    language = detect_language(dir_name)
    if(language == None):
        logger.critical("Language not supported")
        clean_exit(args, logger, dir_name, execution_log)
        
        
    
    game_map = extract_game_map(args)
    #print "here"
    execute_game_map(logger,game_map,args, execution_commands[language].format(dir_name = dir_name), dir_name,execution_log )
    
    #scores = [exec_function(dir_name, args, game)for game in args.game_ids for i in range(args.n_times)]
    #action_file_names = [i for i in range(len(scores))]    
    #print scores, action_file_names
    #logger.info(str(scores)[1:-1])
    #logger.info(str(action_file_names)[1:-1])    

    
   
    clean_exit(args, logger, dir_name, execution_log)
    
if __name__=="__main__":
    # List of games
    # Number of times game is to be executed
    # Zip file name
    # agent ID
    # Run ID
    parser = argparse.ArgumentParser(description='Execute an agent vs a list of games and levels.')
    parser.add_argument('--game_levels', type=str, 
                       help='List of games + ids  to execute',required=True)                  
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
                       
    parser.add_argument('--upload', action='store_const', const=True,
                       help='Upload the scores to the db as well',required=False)
                       
    parser.add_argument('--clean', action='store_const', const=True,
                       help='Should I clean-up after running this',required=False)  
                       
    # Database commands               
    parser.add_argument('--db_properties', type=str,
                       help='Database properties',required=False)      
    
    #print "etf"
                       
    args = parser.parse_args()
    explode_run(args) 
    


