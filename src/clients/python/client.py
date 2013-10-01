from __future__ import print_function
import sys
import simplejson as json
import os


# Can be overwritten by implementation




def queryStateAction(state_str, action):
    action_map = {};
    action_map["action"] = action;
    j_action_map = json.dumps(action_map)

    try:
        sys.stdout.write("1" + j_action_map + ";" + state_str + os.linesep);
        sys.stdout.flush()
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror), file=sys.stderr)
        #
        #exit(0)

    return sys.stdin.readline()[:-1]


def queryStateActionJSON(state, action):
    state_str = json.dumps(state)
    new_state = queryStateAction(state_str, action)
    return json.loads(new_state)


if __name__ == "__main__":
    import mcts_agent as agent

    i = 0
    line = "start"
    while (line != ""):
        #print(str(line) + " " +  str(i), file=sys.stderr)
        line = sys.stdin.readline()
        #print line, i
        if (i == 0):
            #print(str(line) + " " +  str(i), file=sys.stderr)

            action_map = json.loads(line)
            agent.initialise(action_map)
            sys.stdout.write("INIT_DONE" + os.linesep);
            sys.stdout.flush()

        elif (line != ""):
            state_map = json.loads(line)
            action = agent.act(state_map)
            action_map = {}
            action_map["action"] = action
            sys.stdout.write("0" + json.dumps(action_map) + os.linesep);
            sys.stdout.flush()
            #print(str(action_map), file=sys.stderr)

        i += 1