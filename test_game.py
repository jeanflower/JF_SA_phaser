# GATHER REQUIRED FILES
# create a folder for test environment
# copy index.html, renamed to a unique filename.html
# copy assets/paddle.png
# copy phaser.min.js
#
# START WEB SERVER
# python -m http.server
#
# REQUEST PAGE
# open filename.html

# CLEANUP
# ps
# kill -p 'the process ID of the python -m httpserver process'

import os # for sending commands to terminal
import sys # for getting python command line arguments
import time 

unique_name = "test_game_"+str(time.time())

# GATHER REQUIRED FILES
os.system('mkdir '+unique_name)
os.system('mkdir '+unique_name+"/assets")
os.system('cp index.html '+unique_name+"/"+unique_name+".html")
os.system('cp assets/paddle.png '+unique_name+"/assets/paddle.png")

print(sys.argv)

if len(sys.argv) == 1: # no arguments
    os.system('cp phaser.min.js '+unique_name+"/phaser.min.js")
elif sys.argv[1] == "new":
    os.system('cp new_phaser/phaser.min.js '+unique_name+"/phaser.min.js") # doesn't work
elif sys.argv[1] == "old":
    os.system('cp old_phaser/phaser.min.js '+unique_name+"/phaser.min.js") 

print("files copied to "+unique_name)

# START WEB SERVER
import os
os.system('python -m http.server &')

print("server running")

# REQUEST PAGE
os.system("open -n -a \"Google Chrome\" --args \"--new-window\" "
          +"\"http://localhost:8000/"+unique_name+"/"+unique_name+".html\" &")

print("opened web page")

# Let the user try out the game

input("Press Enter to continue...")

# CLEAN UP

# find the process for http.server and kill it
processes = os.popen("ps").read()
for process in processes.splitlines():
    if "http.server" in process:
        pid = process[1:5]
        print("killing process id = "+pid)
        os.system('kill -9 '+pid)
        
print("cleaned up")
