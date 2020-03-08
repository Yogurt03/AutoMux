##automux
# -*- coding: utf-8 -*-

import os, sys
from Module.AMcore import *
from time import sleep as timeout
from termcolor import *

def main():
    banner()
    automux = input(colored("AutoMux >>> ","yellow"))

    if automux == "help":
        help()
        menu = input(colored("AutoMux >>> ","yellow"))
        if menu.strip() == "1" or menu.strip() == "01" or menu.strip() == "change":change()
        elif menu.strip() == "2" or menu.strip() == "02" or menu.strip() == "install":install()
        elif menu.strip() == "3" or menu.strip() == "03" or menu.strip() == "repair":repair_msf()
        elif menu.strip() == "4" or menu.strip() == "04" or menu.strip() == "trojan":msf_mm()
        elif menu.strip() == "5" or menu.strip() == "05" or menu.strip() == "update":update()
        elif menu.strip() == "0" or menu.strip() == "00" or menu.strip() == "exit":sys.exit()
        else:error()

    elif automux.strip() == "1" or automux.strip() == "01" or automux.strip() == "change":change()
    elif automux.strip() == "2" or automux.strip() == "02" or automux.strip() == "install":install()
    elif automux.strip() == "3" or automux.strip() == "03" or automux.strip() == "repair":repair_msf()
    elif automux.strip() == "4" or automux.strip() == "04" or automux.strip() == "trojan":msf_mm()
    elif automux.strip() == "5" or automux.strip() == "05" or automux.strip() == "update":update()
    elif automux.strip() == "0" or automux.strip() == "00" or automux.strip() == "exit":sys.exit()
    elif automux.strip() == "test":
        pwd = os.getcwd()
        print(pwd)
    else:error()  

def help():
    print("\nAutoMux Commands\n========================\n")
    print("    Command           Description\n    -------           -----------")
    print("    01|change        Change source")
    print("    02|install       List installation list")  
    print("    03|repair        Repair MSF database")  
    print("    04|trojan        Generate MSF Trojan")  
    print("    05|update        Update AutoMux")  
    print("    00|exit          Exit AutoMux\n")  

def change():
    print(colored("\n请选择要更换的源:\n","blue"))
    print("    [01]  官方源")
    print("    [02]  清华大学源\n")
    print("    [00]  Bcak Menu\n")
    source = input(colored("AutoMux >>> ","yellow"))

    if source.strip() == "1" or source.strip()  == "01":gfy()
    elif source.strip() == "2" or source.strip()  == "02":qhd()
    elif source.strip()  == "0" or source.strip()  == "00":restart()
    else:error()  

def install():
    print("\n    [01]  Nmap")
    print("    [02]  Hydra")
    print("    [03]  hping3" + colored(" < ","red"))
    print("    [04]  sqlmap")
    print("    [05]  dnsmap")
    print("    [06]  Lazymux")
    print("    [07]  sslscan")
    print("    [08]  RED_HAWK")
    print("    [09]  WebCrack")
    print("    [10]  Bettercap" + colored(" < ","red"))
    print("    [11]  Slowloris")
    print("    [12]  oh-my-zsh")
    print("    [13]  webdirscan")
    print("    [14]  SlowHTTPTest")
    print("    [15]  RouterSploit")
    print("    [16]  Aircrack-ng" + colored(" < ","red"))
    print("    [17]  Metasploit\n")
    print("    [00]  Bcak Menu\n") 
    install = input(colored("AutoMux >>> ","yellow"))

    if install.strip() == "1" or install.strip() == "01":install_nmap()
    elif install.strip() == "2" or install.strip() == "02":install_Hydra()
    elif install.strip() == "3" or install.strip() == "03":install_hping3()
    elif install.strip() == "4" or install.strip() == "04":install_sqlmap()
    elif install.strip() == "5" or install.strip() == "05":install_dnsmap()
    elif install.strip() == "6" or install.strip() == "06":install_lazymux()
    elif install.strip() == "7" or install.strip() == "07":install_sslscan()
    elif install.strip() == "8" or install.strip() == "08":install_RED_HAWK()
    elif install.strip() == "9" or install.strip() == "09":install_WebCrack()
    elif install.strip() == "10":install_bettercap()
    elif install.strip() == "11":install_slowloris()
    elif install.strip() == "12":install_zsh()
    elif install.strip() == "13":install_webdirscan()
    elif install.strip() == "14":install_SlowHTTPTest()
    elif install.strip() == "15":install_RouterSploit()
    elif install.strip() == "16":install_aircrack_ng()
    elif install.strip() == "17":install_msf()
    elif install.strip() == "0" or install.strip() == "00":restart()
    else:
            print(colored("\n输入错误，请重新输入！\n","red"))
            timeout(2)
            restart()      

def update():
    print("\n请选择更新方式:\n")
    print("    [01]  一键安装的更新")
    print("    [02]  克隆安装的更新\n")
    print("    [00]  Bcak Menu\n")
    up = input(colored("AutoMux >>> ","yellow"))

    if up.strip() == "0" or up.strip() == "00" or up.strip() == "exit":sys.exit()
    elif up.strip() == "02" or up.strip() == "2":
        print(colored("\n更新中，请稍候...\n","green"))
        pwd = os.getcwd()
        os.system("cd %s" %pwd)
        os.system("git stash && git pull origin master")
        os.system("cd ~")
        print(colored("\n更新完成AutoMux将在3秒后重启AutoMux\n","green"))
        timeout(3)
        restart()
    elif up.strip() == "01" or up.strip() == "1":   
        print(colored("\n更新中，请稍候...\n","green"))
        os.system("bash $PREFIX/share/AutoMux/script/update.sh")
        print(colored("\n更新完成AutoMux将在3秒后重启AutoMux\n","green"))
        timeout(3)
        restart()
    else:error()
   
def error():   
    print(colored("\n输入错误，请重新输入！\n","red"))
    timeout(2)
    restart() 

if __name__ == "__main__":
	main()
