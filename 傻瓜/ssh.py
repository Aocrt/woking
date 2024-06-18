import paramiko


class ssh:

    def rmrf(hostname, port, username, password):
        print(hostname, port, username, password)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(str(hostname), int(port), str(username), str(password))
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

    def gz(hostname, port, username, password, bb):
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)

        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.put(
            "./file/" + bb + "/download/install.tar.gz",
            "/mnt/nandflash/download/install.tar.gz",
        )
        sftp.put("./file/" + bb + "/tcu_installer", "/mnt/nandflash/tcu_installer")

        sftp.close()

        transport.close()

    def run(hostname, port, username, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)
        commands = [
            "chmod 777 /mnt/nandflash/*",
            "/mnt/nandflash/tcu_installer",
            "reboot",
        ]

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(f"Command:    {command}")
            print(stdout.read().decode())

        client.close()

    def go(hostname, port, username, password, bb):
        ssh.rmrf(hostname, port, username, password)
        ssh.gz(hostname, port, username, password, bb)
        ssh.run(hostname, port, username, password)
