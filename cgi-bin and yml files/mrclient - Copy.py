#!/usr/bin/python36

print("content-type: text/html")

print("")


import cgi
import subprocess as sp

form=cgi.FieldStorage()
c=form.getvalue('c')
#print(username)

#x=sp.getstatusoutput("sudo ansible-playbook mapreduceclient.yml --extra-vars='c={}'".format(c))
#print(x)
#if x[0]==0:
print("<h1>location: 192.168.43.224/hadoop.html</h1>")                                                                                       
