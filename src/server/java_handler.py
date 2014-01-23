from subprocess import Popen, PIPE,check_output
import os


def compile_java(username, dir_name, vgdl_jar, file_name):
    #print vgdl_jar
    javac_command = "cd " + dir_name + ";"
    javac_command+= "javac -cp " +  vgdl_jar + " "
    javac_command+=username + "/" + file_name
    p = Popen(javac_command, shell=True, bufsize=1000000,
          stderr=PIPE, stdout=PIPE, close_fds=True)

    out, err = p.communicate()
    #print out,err
    return out,err

if __name__=="__main__":
    username = "ssamot"
    compile_java("ssamot", "./tmp", "Agent.java")
    #game = load_game("examples.gridphysics.frogs")
    #print mediate(game,"python /home/ssamot/projects/vgdl/vgdl_competition/src/clients/python/client.py")
    #args = ["java", "-cp" ]
    #grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
    #p.communicate()