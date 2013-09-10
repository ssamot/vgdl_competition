from subprocess import Popen, PIPE,check_output
import subprocess
import json
from time import sleep


DUMMY_COMMAND = {}
DUMMY_COMMAND["Dummy"] = 1
DUMMY_COMMAND["Dummy"] = 2

END_COMMAND = "END_COMMAND\n"


def mediate(iterations, args):
    p = Popen(args, shell=True, bufsize=1000000,
          stdin=PIPE, stdout=PIPE, close_fds=True)
    out_buffer = []
    p.stdin.write("init\n");p.stdin.flush()
    #sleep(10)
    #p.stdin.write("B\n");p.stdin.flush()
    for iteratin in range(iterations):
        reply = False
        line = p.stdout.readline()
        if line.endswith(END_COMMAND):
            line = line[:-len(END_COMMAND)]
            reply = True
        
        out_buffer.append(line)
        print line,reply
        json_str = "".join(out_buffer)        
        
        if(reply):
            json_str = "".join(out_buffer)
            #print json_str
            out_buffer = []
            p.stdin.write("test\n");p.stdin.flush()
            print "sdfsfd",line
            reply = False
            
def compile_java():
    p = Popen("javac Agent.java", shell=True, bufsize=1000000,
          stderr=PIPE, stdout=PIPE, close_fds=True)
          
    out, err = p.communicate()
    print out
    print err

if __name__=="__main__":
    compile_java()
    mediate(5,"java Agent")
    #args = ["java", "-cp" ]
    #grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
    #p.communicate()
    
            
            
        
        
          
         
   
     