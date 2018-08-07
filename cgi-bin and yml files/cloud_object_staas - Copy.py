import  socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM , 0)
s.bind(  ( "192.168.0.104", 1111 ) )

c_user_name = s.recvfrom(20)

c_user_name = c_user_name[0].decode()
print(c_user_name)


c_drive_size = s.recvfrom(20)

c_drive_size = c_drive_size[0].decode()
print(c_drive_size)


lv_create = "lvcreate --size {size}G --name {name}   vgcloud".format(size=c_drive_size,      name=c_user_name)

subprocess.getoutput(lv_create)

lv_format = "mkfs.ext4  /dev/vgcloud/{name}".format(name=c_user_name)

subprocess.getoutput(lv_format)
user_dir = "mkdir /cloud/{name}".format(name=c_user_name)


subprocess.getoutput(user_dir)

part_mount = "mount /dev/vgcloud/{name}  /cloud/{name}".format(name=c_user_name)


subprocess.getoutput(part_mount)



share_nfs = "echo  '/cloud/{name} 192.168.0.107(rw,no_root_squash)'  >> /etc/exports".format(name=c_user_name)

subprocess.getoutput(share_nfs)

nfs_service = "systemctl  restart  nfs"
subprocess.getoutput(nfs_service)

s.sendto( b"success",  ("192.168.0.107", 2222))










