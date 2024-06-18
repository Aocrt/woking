import show

if __name__ == "__main__":
    Show = show.show()
    text = """
            此程序为刷TCU程序

            写入程序请输入：
            1.stcu 3000     2.北变      3.昇伟      4.其他tcu

            改本机IP请输入:
            a.stcu 3000     b.北变      c.昇伟.     d.其他tcu

            ###在123刷机失败的情况下选择4根据提示操作###
        """
    a = input(text)
    while a == "exit":
        if a == "1":
            Show.show1(0)
        elif a == "2":
            Show.show2(1)
        elif a == "3":
            Show.show3(2)
        elif a == "4":
            Show.show4()
        elif a == "a":
            Show.showa(0)
        elif a == "b":
            Show.showb(1)
        elif a == "c":
            Show.showc(2)
        elif a == "d":
            Show.showd()
        else:
            Show.showElse()
        a = input(text)
