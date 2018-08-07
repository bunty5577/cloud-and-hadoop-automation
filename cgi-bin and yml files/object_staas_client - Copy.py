import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,  0)


s.bind( ("192.168.0.107", 2222) )


print('''
press 1: create create drive
press 2: extend drive
''')


ch  = raw_input("enter ur choice : ")

if int(ch) == 1:
	print("creating ....")
	user_name =  raw_input("enter ur user name : ")
	# user_name = bytes(user_name, 'utf-8')
	s.sendto(user_name , ("192.168.0.104", 1111))
	size_drive = raw_input("enter size of new drive in GB : ")
	# size_drive = bytes(size_drive, 'utf-8')
	s.sendto(size_drive , ("192.168.0.104", 1111))

elif int(ch) == 2:
	print("extend")
else:
	print("not supported")

status = s.recvfrom(20)

#status =  status[0].decode()

if status[0] == "success":
	print("hi")
	os.system("mkdir /media/{0}".format(user_name))
	mount_cloud = "mount  192.168.0.104:/cloud/{0}  /media/{0}".format(user_name)
#	subprocess.getoutput(mount_cloud)
	os.system(mount_cloud)



