from ip import *
from ssh import *


class show:

    ipAddr = ["192.168.0.42", "192.168.2.123", "10.100.100.20"]
    ipMask = ["255.255.255.0", "255.255.255.0", "255.255.0.0"]
    username = ["hstrasonm", "root", "sanway"]
    password = ["eX7tc2fD5", "1", "sanway1929"]
    bb = [
        "2.44",
        "2.52",
        "2.56.8",
        "2.73.9",
        "2.73.10",
        "2.74.3",
        "2.80",
        "2.90",
        "3.10",
    ]

    def __init__(self):
        pass

    def showElse(self):
        print("非法输入")

    def show1(self, num):
        ssh.go(self.ipAddr[num], 22, self.username[num], self.password[num], "3.10")

    def show2(self, num):
        ssh.go(self.ipAddr[num], 22, self.username[num], self.password[num], "2.80")

    def show3(self, num):
        ssh.go(self.ipAddr[num], 22, self.username[num], self.password[num], "2.80")

    def show4(self):
        text = """
            2.44    2.52    2.56.8    2.73.9    2.73.10    2.74.3    2.80    2.90    3.10
            请输入版本号:
        """
        ipAddr = input("请输入TCU地址:")
        username = input("请输入用户名")
        password = input("请输入密码")
        bb = input(text)
        ssh.go(ipAddr, 22, username, password, bb)

    def showa(self, num):
        ipList = self.ipAddr[num].split(".")
        ip = f"{ipList[0]}.{ipList[1]}.{ipList[2]}.200"
        print(ip().set_ip("以太网", ip, self.ipMask[num]))

    def showb(self, num):
        ipList = self.ipAddr[num].split(".")
        ip = f"{ipList[0]}.{ipList[1]}.{ipList[2]}.200"
        print(ip().set_ip("以太网", ip, self.ipMask[num]))

    def showc(self, num):
        ipList = self.ipAddr[num].split(".")
        ip = f"{ipList[0]}.{ipList[1]}.{ipList[2]}.200"
        print(ip().set_ip("以太网", ip, self.ipMask[num]))

    def showd(self):
        ipAddr = input("请输入TCU地址:")
        ipMask = input("请输入子网掩码:")
        ipList = ipAddr.split(".")
        ip = f"{ipList[0]}.{ipList[1]}.{ipList[2]}.200"
        print(ip().set_ip("以太网", ip, ipMask))
