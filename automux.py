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
    print("    [03]  生成Msf木马")    
    print("    [04]  修复Msf数据库\n")  
    print("    [00]  退出AutoMux\n")
    automux = input(colored("AutoMux >>> ","yellow"))

    if automux.strip() == "1" or automux.strip() == "01":
        print(colored("\n请选择要更换的源:\n","blue"))
        print("    [01]  官方源")
        print("    [02]  清华大学源\n")
        print("    [00]  返回主菜单\n")
        source = input(colored("AutoMux >>> ","yellow"))

        if source.strip() == "1" or source.strip()  == "01":gfy()
        elif source.strip() == "2" or source.strip()  == "02":qhd()
        elif source.strip()  == "0" or source.strip()  == "00":restart()
        else:
            print(colored("\n输入错误，请重新输入！","red"))
            timeout(2)
            restart()
    
    elif automux.strip() == "2" or automux.strip() == "02":
        print("\n    [01]  Nmap")
        print("    [02]  Hydra")
        print("    [03]  Lazymux")
        print("    [04]  ohmyzsh")
        print("    [05]  Metasploit\n")
        print("    [00]  返回主菜单\n") 
        install = input(colored("AutoMux >>> ","yellow"))

        if install.strip() == "1" or install.strip() == "01":install_nmap()
        elif install.strip() == "2" or install.strip() == "02":install_Hydra()
        elif install.strip() == "3" or install.strip() == "03":install_lazymux()
        elif install.strip() == "4" or install.strip() == "04":install_zsh()
        elif install.strip() == "5" or install.strip() == "05":install_msf()
        elif install.strip() == "0" or install.strip() == "00":restart()
        else:
            print(colored("\n输入错误，请重新输入！","red"))
            timeout(2)
            restart()           
    elif automux.strip() == "3" or automux.strip() == "03":msf_mm()
    elif automux.strip() == "4" or automux.strip() == "04":repair_msf()
    elif automux.split() == "update":
        os.system("cd $PREFIX/share/AutoMux")
        os.system("chmod +x update.sh")
        os.system("./update.sh")
    elif automux.strip() == "0" or automux.strip() == "00" or automux.strip() == "exit":sys.exit()
    else:
        print(colored("\n输入错误，请重新输入！\n","red"))
        timeout(2)
        restart()

if __name__ == "__main__":
	main()
