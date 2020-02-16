##automux
# -*- coding: utf-8 -*-

import os, sys
from Module.AMcore import *
from time import sleep as timeout
from termcolor import *

def main():
    banner()
    print("    [01]  更换Termux源")
    print("    [02]  列出安装列表")
    print("    [03]  修复Msf数据库")
    print("    [04]  添加Sudo命令(Root)")   
    print("    [05]  更新AutoMux\n")
    print("    [00]  退出AutoMux")
    automux = input("AutoMux >>> ")

    if automux.strip() == "1" or automux.strip() == "01":
        print("请选择要更换的源:")
        print("    [01]  官方源")
        print("    [02]  清华大学源\n")
        print("    [00]  返回主菜单\n")
        source = input("AutoMux >>> ")

        if source.strip() == "1" or source.strip()  == "01":gfy()
        elif source.strip() == "2" or source.strip()  == "02":qhd()
        elif source.strip()  == "0" or source.strip()  == "00":restart()
        else:
            print(colored("\n输入错误，请重新输入！","red"))
            timeout(2)
            restart()
    
    elif automux.strip() == "2" or automux.strip() == "2":
        print("\n    [01]  Nmap")
        print("    [02]  Lazymux")
        print("    [03]  Metasploit\n")
        print("    [00]  返回主菜单\n") 
        install = input("AutoMux >>> ")

        if install.strip() == "1" or install.strip() == "01":install_nmap()
        elif install.strip() == "2" or install.strip() == "02":install_lazymux()
        elif install.strip() == "3" or install.strip() == "03":install_msf()
        elif install.strip() == "0" or install.strip() == "00":restart()
        else:
            print(colored("\n输入错误，请重新输入！","red"))
            timeout(2)
            restart()           
    elif automux.strip() == "3" or automux.strip() == "03":repair_msf()
    elif automux.strip() == "4" or automux.strip() == "04":install_sudo()
    elif automux.strip() == "5" or automux.strip() == "05":upgrade_AutoMux()
    elif automux.strip() == "0" or automux.strip() == "00":sys.exit()
    else:
        print(colored("\n输入错误，请重新输入！\n","red"))
        timeout(2)
        restart()

if __name__ == "__main__":
	main()