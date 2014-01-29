from subprocess import Popen, PIPE,check_output
import os


def compile_java(username, dir_name, vgdl_jar, file_name):
    #print vgdl_jar
    #print dir_name + "------------------"
    javac_command = "cd " + dir_name + ";"
    javac_command+= "javac -cp " +  vgdl_jar + " "
    javac_command+="$(find " + dir_name + "  | grep \\\.java)"
    #print javac_command
    p = Popen(javac_command, shell=True, bufsize=1000000,
          stderr=PIPE, stdout=PIPE, close_fds=True)

    out, err = p.communicate()
    #print out,err
    return out,err


def run_java(username, dir_name, vgdl_jar, game_map, game_level, action_filename):
    #print vgdl_jar
    #java -cp /home/ssamot/projects/vgdl/java-vgdl/build/dist/vgdl.jar: core.competition.AgentExecuto
    java_command = "cd " + dir_name + ";"
    java_command+= "java -cp " +  vgdl_jar + ": "
    java_command+="core.competition.AgentExecutor " + game_map + " " + game_level + " " + username + ".Agent " + action_filename
    print java_command
    p = Popen(java_command, shell=True, bufsize=1000000,
          stderr=PIPE, stdout=PIPE, close_fds=True)

    out, err = p.communicate()
    print out,err
    if(err == ""):
        result = out.split("\n")[-2]
        score = float(result.split("Score: ")[-1])
        win = result[5:].split(".")[0]
        print score, win
        score = float(score)
    else:
        score = -1
        win = "loss"
    #p.kill()
    return win,score,[],out,err


if __name__=="__main__":
    username = "ssamot"
    compile_java("ssamot", "./tmp", "Agent.java")
    #game = load_game("examples.gridphysics.frogs")
    #print mediate(game,"python /home/ssamot/projects/vgdl/vgdl_competition/src/clients/python/client.py")
    #args = ["java", "-cp" ]
    #grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
    #p.communicate()