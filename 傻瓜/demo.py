import paramiko


hostname = "192.168.2.123"
port = 22
username = "root"
password = "1"
# path='c:/file'
print(type(hostname), type(port), type(username), type(username))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)
commands = [
    "chmod 777 /mnt/nandflash/*",
    "rm -rf /mnt/nandflash/*",
    "mkdir /mnt/nandflash/download",
    "chmod 777 /mnt/nandflash/*",
]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(f"Command:    {command}")
    print(stdout.read().decode())

client.close()
