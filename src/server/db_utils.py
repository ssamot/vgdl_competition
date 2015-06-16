#!/usr/bin/python
# Python DB APIs:
#for more: http://www.mikusa.com/python-mysql-docs/index.html
#and more: http://zetcode.com/db/mysqlpython/
#and else: http://mysql-python.sourceforge.net/MySQLdb.html

import MySQLdb as mdb
import itertools
from pprint import pprint
import ConfigParser

def db_connect(properties_file):
    config = ConfigParser.ConfigParser()
    #print properties_file
    #open(properties_file)
    config.read(properties_file)
    #print config.sections()
    host = config.get("Database", "host")
    user = config.get("Database", "user")
    passwd = config.get("Database", "passwd")
    db_name = config.get("Database", "db")    
    db = mdb.connect(host=host, # your host, usually localhost
                     user=user, # your username
                     passwd=passwd, # your password
                     db=db_name) # name of the data base
                     
    return db

# Gets all game info from a given game ID. Data returned in a dictionary.
def get_game_info(db, game_id):
    #This cursor allows access as in a dictionary:
    cur = db.cursor(mdb.cursors.DictCursor)
    
    cur.execute("SELECT * from games where game_id = %s", [game_id])
    game_data = cur.fetchone()
    return game_data
    


# Gets all info from all levels given a game ID. Data returned in array.
def get_levels_from_game(db, game_id):

    #This cursor allows access as AN ARRAY:
    cur = db.cursor()

    cur.execute("SELECT * from levels where game_id = %s", [game_id])
    levels = cur.fetchall()

    return levels


# Gets ids from all levels given a game ID. Data returned in array
def get_level_ids_from_game(db, game_id):

    #This cursor allows access as AN ARRAY:
    cur = db.cursor()

    cur.execute("SELECT level_id from levels where game_id = %s", [game_id])
    levels = cur.fetchall()
    level_ids = list(itertools.chain.from_iterable(levels))

    return level_ids


# Gets all info from a level given a level ID. Data returned in a dictionary
def get_level_info(db, level_id):

    #This cursor allows access as in a dictionary:
    cur = db.cursor(mdb.cursors.DictCursor)

    cur.execute("SELECT * from levels where level_id = %s", [level_id])
    level = cur.fetchone()

    return level


if __name__=="__main__":
 
  #Connect to database.
    try:
        print ""
        
    
        print " ------- Game info from game_id ------- "
        game_data = get_game_info(db,1)
        pprint(game_data)
        print ""
    
        print " ------- Level IDs from game_id ------- "
        level_ids_from_game = get_level_ids_from_game(db,1)
        pprint(level_ids_from_game)
        print ""
    
        print " ------- Levels from game_id ------- "
        levels = get_levels_from_game(db,1)
        print(levels)
        print ""
    
        print " ------- Level info from level_id ------- "
        level = get_level_info(db,3)
        pprint(level)
        print ""

    except Exception, e:
        print "Error accessing database, " + str(e)

# -*- coding: utf-8 -*-

