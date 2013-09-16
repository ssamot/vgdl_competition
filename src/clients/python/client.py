from __future__ import print_function
import sys
import simplejson as json
import os


# Can be overwritten by implementation
import agent

if __name__=="__main__":

    i = 0
    line = "start"
    while(line !=""):
        #print(str(line) + " " +  str(i), file=sys.stderr)
        line = sys.stdin.readline()
        #print line, i
        if(i ==0):
            action_map = json.loads(line)
            agent.initialise(action_map)
            sys.stdout.write ("INIT_DONE" + os.linesep);sys.stdout.flush()

        elif(line !=""):
            #print(str(line) + " " +  str(i), file=sys.stderr)
            state_map = json.loads(line)
            action = agent.act(state_map)
            action_map = {}
            action_map["action"] = action
            sys.stdout.write (json.dumps(action_map) + os.linesep);sys.stdout.flush()
            #print(str(action_map), file=sys.stderr)

        i+=1
