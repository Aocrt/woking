import os, re


class ip:

    def __init__(self):
        pass
        # self.ip_list = self.get_ip()

    def set_ip(self, name, ip, mask):

        result = os.popen(
            f"netsh interface ip set address name={name} static {ip} {mask}"
        )
        res = result.read()
        return res

    def get_ip(self):

        result = os.popen("ipconfig")
        res = result.read()

        resultlist = re.findall(
            """(?<=以太网适配器 ).*?(?=:)|(?<=无线局域网适配器 ).*?(?=:)""", res
        )

        print(resultlist)

        return resultlist
