from subprocess import Popen, PIPE
import json


DUMMY_COMMAND = {}
DUMMY_COMMAND["Dummy"] = 1
DUMMY_COMMAND["Dummy"] = 2

END_COMMAND = "END_COMMAND"


def mediate(iterations, args):
    p = Popen(args, shell=True, bufsize=1000000,
          stdin=PIPE, stdout=PIPE, close_fds=True)
    out_buffer = [];
    for iteration in range(iterations):
        reply = False
        line = p.stdout.readline()
        if line.endswith(END_COMMAND):
            line = line[:-len(END_COMMAND)]
            reply = True
        
        out_buffer.append(line)
        
        json_str = "".join(out_buffer)        
        
        if(reply):
            json_str = "".join(out_buffer)
            print json_str
            out_buffer = []
            p.stdin.write(DUMMY_COMMAND)
            reply = False

if __name__=="__main__":
    args = ["java", "-cp" ]
    #grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
    #p.communicate()
    
            
            
        
        
          
         
   
     