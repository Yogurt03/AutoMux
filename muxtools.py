
import os, sys
from Module.MTcore import *
from time import sleep as timeout


def main():
    banner()
    print("    [1]  更换Termux源")
    print("    [2]  安装Lazymux")
    print("    [3]  安装Metasploit")
    print("    [4]  修复msf数据库")
    print("\n    [0]  退出Muxtoosl")
    XXX = input("请输入要运行的指令 >>> ")
    if XXX == "1": #更换Termux源
        print("    [1] 更换官方源")
        print("    [2] 更换清华大学源")
        print("    [0] 返回主菜单")
        XX = input("请输入要运行的命令 >>> ")
        if XX == "1": #更换官方源
            gfy()
            print("更换成功，2秒后重启程序")
            time.sleep(2)
            restart()
        elif XX == "2": #更换清华大学源
            qhd()
            print("更换成功，2秒后重启程序")
            time.sleep(2)
            restart()
        elif XX == "0": #返回主程序
            os.system("clear")
            restart()
        else:
            print("输入错误请重新输入!")
            timeout(2)
            os.system("clear")
            restart()
    elif XXX == "2": #安装Lazymux
        install_lazymux()
        print("安装成功，2秒后重启程序")
        time.sleep(2)
        restart()
    elif XXX == "3": #安装MSF
        install_msf()
        print("安装成功，2秒后重启程序")
        time.sleep(2)
        restart()
    elif XXX == "4":
        repair()
        print("修复成功，2秒后重启程序")
        time.sleep(2)
        restart()
    elif XXX == "0": #退出程序
        sys.exit()
    else:
        print("输入错误请重新输入!")
        timeout(2)
        os.system("clear")
        restart()



if __name__ == "__main__":
	main()