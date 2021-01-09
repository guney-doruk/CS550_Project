import paramiko
import ast 
import os

def connection(image):
    host = '3.12.102.21'    
    user = 'ec2-user'
    pem = 'pem-file.pem'
    instance = user+'@'+host

    os.system(f'cmd /c "scp -i {pem} {image} {instance}:/home/ec2-user/CS550_Project_1"')


    key = paramiko.RSAKey.from_private_key_file(pem)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname = host, username = user, pkey = key)

    stdin, stdout, stderr = ssh_client.exec_command(f'./CS550_Project_1/sex.py {image}')

    labels = stdout.readlines()
    out = []
    for i in labels:
        res = ast.literal_eval(i)
        out.append(res)
    ssh_client.close()
    return out
