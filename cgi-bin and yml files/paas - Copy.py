#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess

form=cgi.FieldStorage()
username=form.getvalue('username')
print(username)
choice=form.getvalue('python')
print(choice)
out=subprocess.getstatusoutput("sudo docker run -dit --name {0} -p 5678:4200 python:v1".format(username))
if out[0]==0:
   print("Python successfully")
else:
   print("Not")

print("""
<div>
<a href="http://192.168.43.224:5678" target='f1'><input type=submit value="Launch python"></input></a>
</div>
<div>
<iframe width="100%" name='f1' ></iframe>
</div>
<div>
<input type=submit value="Stop Docker"></input>

</div>
""")

