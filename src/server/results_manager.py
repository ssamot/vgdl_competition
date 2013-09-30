#!/usr/bin/python
# Python DB APIs:
#for more: http://www.mikusa.com/python-mysql-docs/index.html
#and more: http://zetcode.com/db/mysqlpython/
#and else: http://mysql-python.sourceforge.net/MySQLdb.html

import MySQLdb as mdb
import argparse
import datetime as dt
import db_utils
import numpy as np


def calc_score(games):
    #Sum of the scores on each game, for now.
    s = 0
    for game in games:
        s+=game[2]
    return s
    
    
def process_log(args):

    date_format = '%Y-%m-%d %H:%M:%S'

    #Connect to database.
  
    db = db_utils.db_connect(args.db_properties)
    #cur = db.cursor() 
    #This cursor allows access as in a dictionary:
    cur = db.cursor(mdb.cursors.DictCursor)

    score = -1
    log_file = args.execution_log
  
    now = dt.datetime.now()
    current_timestamp = now.strftime(date_format)


    log_level = "INFO";
    games = []
    with open(args.execution_log, 'r') as log_file :
        for i, line in enumerate(log_file):
            if(i == 1):
                run_id = long(line.split(" ")[-1])
            if(i == 2):
                user_id = long(line.split(" ")[-1])
            if(i>2):
                splitted = line[:-1].split(" ")
                print run_id, user_id, splitted
                if(splitted[2] != "INFO" ):
                    # check if we have reached the end of the file
                    current_timestamp = now.strftime(splitted[0] + " " + splitted[1] )
                    if(splitted[2] == "DEBUG"):
                        break
                    else:
                        log_level = splitted[2]
                        error_msg = " ".join(map(str,splitted[3:]))
                        break
                else:
                    g_split = splitted[3].split(",")
                    game_id = long(g_split[0][-1:]) 
                    l_split = splitted[4].split(",")
                    level_id = long(l_split[0][-1:]) 
                      
                    score = long(splitted[5])
                    action_file =  splitted[6]
                    games.append((game_id,level_id,score, action_file))
                    
                
    print log_level, run_id, user_id, games, current_timestamp
    #exit(0)
            

    if log_level == 'INFO':
        #total score:
        score = calc_score(games)
        #Set controller status to the proper new state:
        cur.execute("UPDATE runs set run_state = 'ok', end_time = %s, run_log_file = %s, score = %s where run_id = %s", (current_timestamp,args.execution_log,score,run_id))
        cur.execute("UPDATE users set controller_status = 'OK' where user_id = %s", (user_id))

	#One match per game played into the database:
        for game in games:		
            game_id = game[0]
            level_id = game[1]
            score = game[2]
            actions_file = game[3]
    
            cur.execute("REPLACE INTO matches (run_id,level_id,game_id,user_id,human_play,actions_file,score) VALUES (%s,%s,%s,%s,0,%s,%s)",(run_id,level_id,game_id,user_id,actions_file,score))

    elif log_level == 'ERROR':
        #Set controller status to the proper new state:
        cur.execute("UPDATE runs set run_state = 'crash', end_time = %s, run_log_file = %s, run_msg = %s where run_id = %s", (current_timestamp,args.execution_log,error_msg,run_id))
        cur.execute("UPDATE users set controller_status = 'crash' where user_id = %s", (user_id))

    elif log_level == 'CRITICAL':
        print  (current_timestamp,args.execution_log,error_msg,run_id)
        #Set controller status to the proper new state:
        cur.execute("UPDATE runs set run_state = 'failed', end_time = %s, run_log_file = %s, run_msg = %s where run_id = %s", (current_timestamp,args.execution_log,error_msg,run_id))
        cur.execute("UPDATE users set controller_status = 'failed' where user_id = %s", (user_id))



if __name__=="__main__":
    # List of games
    # Number of times game is to be executed
    # Zip file name
    # agent ID
    # Run ID
    parser = argparse.ArgumentParser(description='Update database results based on an execution.log.')
    parser.add_argument('--execution_log', type=str, 
                       help='The log of results to process ',required=True)                  
                       
    # Database commands               
    parser.add_argument('--db_properties', type=str,
                       help='Database properties',required=True)      
    
                       
                       
    args = parser.parse_args()
    process_log(args)
