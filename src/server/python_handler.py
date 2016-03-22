from subprocess import Popen, PIPE,check_output
import os
import logging




def run_python(username, dir_name, vgdl_jar, game_map, game_level, action_filename, logger, python_command):
    #print vgdl_jar
    #java -cp /home/ssamot/projects/vgdl/java-vgdl/build/dist/vgdl.jar: core.competition.AgentExecuto
    java_command = "cd " + dir_name + "/" + username + ";"
    java_command+= "java -cp " +  vgdl_jar + ": -Xms512m -Xmx2048m "
    java_command+="core.competition.AgentExecutorLearning " + game_map + " " + game_level
    ## mega string to handle crap
    java_command+= " " + python_command + " agent.Agent'" + " "
    java_command+=action_filename + " "
    java_command+="true"


    logger.critical(java_command)
    p = Popen(java_command, shell=True, bufsize=1000000,
          stderr=PIPE, stdout=PIPE, close_fds=True)

    out, err = p.communicate()
    print out,err
    if(err == ""):
        result = out.split("\n")[-2]
        win_str, score_str, time_str = result.split(",")
        score = float(score_str.split(":")[-1])
        win = int(win_str.split(":")[-1])
        time = int(time_str.split(":")[-1])
        #print score, win, time
        score = float(score)
    else:
        score = -9999
        win = -100
        time = 0
    #p.kill()
    return win,score,time, [],out,err


if __name__=="__main__":
    username = "ssamot"
