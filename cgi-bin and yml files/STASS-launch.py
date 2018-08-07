#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print("")


print("""

<!DOCTYPE html>
<html>
<head style="background-color:Lavender;">
  <title>Object STAAS</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="style2.css">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  body {
      position: relative; 
  }	
 
  .navbar {
      margin-bottom: 0px;
	  width:100%;
	  
  }

	.button2:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}
  
  .div5 img:hover{
   opacity: 0.9;
    filter: alpha(opacity=90);
  }
	
	.carousel-inner > .item > img,
  .carousel-inner > .item > a > img {
      width: 100%;
      margin: auto;
  }
  .carousel-content{
  position:absolute;
  bottom:10%;
  left:5%;
  z-index:20;
  color:white;
  }
  
  
  
  </style>
</head>

<body style="background:url(staas.jpg); background-attachment:fixed; background-repeat:repeat; background-size:100% 100%;">

<div>
	<div>


	<nav class="navbar navbar-inverse navbar-fixed-top" style="background-color:black; ">
	  <div class="container-fluid">
	    <div class="navbar-header">
	      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>                        
	      </button>
	     <!-- <p style="margin-top:7px;"><span class="icon-bar" style="font-family:AR DESTINE; font-size:24px; color:white; text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;margin-bottom:-5px; margin-left:5px; ">Automation</span></p>     -->
	    </div>
	    <div class="collapse navbar-collapse" id="myNavbar">
	      <ul class="nav navbar-nav" style="float:right">
		
		<li><a  href="mmw1.html"  style="color:white; font-size:24px; text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;" >Home</a></li>
		<li><a href="about1.html" style="color:white; font-size:24px;">About Us</a></li>
		<li><a href="work.html" style="color:white; font-size:24px;">Our Service</a></li>
			<li><a href="contact1.html" style=" color:white; font-size:24px;">Contact Us</a></li>
		
	      </ul>
	      
	    </div>
	  </div>
	</nav>
	</div>
	
		<div style="background-color:white; opacity: 0.8; filter: alpha(opacity=90);margin-top:50px;" >
	<center><h2 style="font-family:Times New Roman; color:Black; font-size:70px;">Storage As A Service</h2></center>
	</div>	



""")






form=cgi.FieldStorage()
cname=form.getvalue('cname')
sname=int(form.getvalue('sname'))
#s=s + 'm'
#print(form)
#print(cname,sname)
#if type(sname)==int:
  # sname=x
#else:
  # print("PLEASE ENTER THE SIZE IN INTEGER")
#sp.getoutput("sudo cd ansible/")
stasslaunch=sp.getstatusoutput('sudo ansible-playbook stass.yml --extra-vars="x={c} y={s}"'.format(c=cname,s=sname))
#print(stasslaunch)
if stasslaunch[0]==0:
   print("<center><b><h1>Storage successfully alloted </h1></b></center>")
   print("")
else:
   print("<center><b><h1>Storage successfully alloted</h1></b></center>")






















