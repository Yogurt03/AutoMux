##automux
# -*- coding: utf-8 -*-

import os, sys
from Module.AMcore import *
from Module.banner import banner
from time import sleep as timeout
from termcolor import *

class install:
    def xxsj():
        print("\n    [01] Nmap")
        print("    [02] Sqlmap")
        print("    [03] RED_HAWK")
        print("    [04] webdirscan")
        print("    [05] dnsmap\n")
        print("    [00] Bcak Menu\n")
        xxsj = input(colored("AutoMux >>> ","yellow"))
        if xxsj.strip() == "1" or xxsj.strip() == "01":install_nmap()
        elif xxsj.strip() == "2" or xxsj.strip() == "02":install_sqlmap()
        elif xxsj.strip() == "3" or xxsj.strip() == "03":install_RED_HAWK()
        elif xxsj.strip() == "4" or xxsj.strip() == "04":install_webdirscan()
        elif xxsj.strip() == "5" or xxsj.strip() == "05":install_dnsmap()
        elif xxsj.strip() == "0" or xxsj.strip() == "00":restart()
        else:error()

    def ldsm():
        print("\n    [01] Nmap")
        print("    [02] RED_HAWK")
        print("    [03] sqlmap")
        print("    [04] RouterSploit")
        print("    [05] sslscan\n")
        print("    [00] Bcak Menu\n")
        ldsm = input(colored("AutoMux >>> ","yellow"))
        if ldsm.strip() == "1" or ldsm.strip() == "01":install_nmap()
        elif ldsm.strip() == "2" or ldsm.strip() == "02":install_RED_HAWK()
        elif ldsm.strip() == "3" or ldsm.strip() == "03":install_sqlmap()
        elif ldsm.strip() == "4" or ldsm.strip() == "04":install_RouterSploit
        elif ldsm.strip() == "5" or ldsm.strip() == "05":install_sslscan()
        elif ldsm.strip() == "0" or ldsm.strip() == "00":restart()
        else:error()

    def ylce():
        print("\n    [01] Slowloris")
        print("    [02] Aircrack-ng" + colored(" * ","red"))
        print("    [03] Hydra")
        print("    [04] hping3" + colored(" * ","red"))
        print("    [05] SlowHTTPTest\n")
        print("    [00] Bcak Menu\n")
        ylce = input(colored("AutoMux >>> ","yellow"))
        if ylce.strip() == "1" or ylce.strip() == "01":install_slowloris()
        elif ylce.strip() == "2" or ylce.strip() == "02":install_aircrack_ng()
        elif ylce.strip() == "3" or ylce.strip() == "03":install_Hydra()
        elif ylce.strip() == "4" or ylce.strip() == "04":install_hping3()
        elif ylce.strip() == "5" or ylce.strip() == "05":install_SlowHTTPTest()
        elif ylce.strip() == "0" or ylce.strip() == "00":restart()
        else:error()      

    def mmgj():
        print("\n    [01] Hydra")
        print("    [02] Cupp")
        print("    [03] Crunch")
        print("    [04] Aircrack-ng" + colored(" * ","red"))
        print("    [05] HashBuster")
        print("    [06] WebCrack\n")
        print("    [00] Bcak Menu\n")
        mmgj = input(colored("AutoMux >>> ","yellow"))
        if mmgj.strip() == "1" or mmgj.strip() == "01":install_Hydra()
        elif mmgj.strip() == "2" or mmgj.strip() == "02":install_Cupp()
        elif mmgj.strip() == "3" or mmgj.strip() == "03":install_Crunch()
        elif mmgj.strip() == "4" or mmgj.strip() == "04":install_aircrack_ng()
        elif mmgj.strip() == "5" or mmgj.strip() == "05":install_HashBuster()
        elif mmgj.strip() == "6" or mmgj.strip() == "06":install_WebCrack()
        elif mmgj.strip() == "0" or mmgj.strip() == "00":restart()
        else:error() 

    def xtqp():
        print("\n    [01] Bettercap\n" + colored(" * ","red"))
        print("    [00] Bcak Menu\n")
        xtqp = input(colored("AutoMux >>> ","yellow"))
        if xtqp.strip() == "1" or xtqp.strip() == "01":install_bettercap()
        elif xtqp.strip() == "0" or xtqp.strip() == "00":restart()
        else:error() 

    def lygj():
        print("\n    [01] Metasploit")
        print("    [02] Sqlmap")
        print("    [03] Routersploit\n")
        print("    [00] Bcak Menu\n")
        lygj = input(colored("AutoMux >>> ","yellow"))
        if lygj.strip() == "1" or lygj.strip() == "01":install_msf()
        elif lygj.strip() == "2" or lygj.strip() == "02":install_sqlmap()
        elif lygj.strip() == "3" or lygj.strip() == "03":install_RouterSploit()
        elif lygj.strip() == "0" or lygj.strip() == "00":restart()
        else:error() 

    def Other(): 
        print("\n    [01] Lazymux")
        print("    [02] oh-my-zsh\n")
        print("    [00] Bcak Menu\n")
        other = input(colored("AutoMux >>> ","yellow"))
        if other.strip() == "1" or other.strip() == "01":install_lazymux()
        elif other.strip() == "2" or other.strip() == "02":install_zsh()
        elif other.strip() == "0" or other.strip() == "00":restart()
        else:error() 
        

def help():
    print("\nAutoMux Commands\n========================\n")
    print("    Command           Description\n    -------           -----------")
    print("    01 change         Change source")
    print("    02 install        List installation list")  
    print("    03 repair         Repair MSF database")  
    print("    04 trojan         Generate MSF Trojan")  
    print("    05 update         Update AutoMux")  
    print("    00 exit           Exit AutoMux\n") 

def main():
    banner()
    automux = input(colored("AutoMux >>> ","yellow"))

    if automux == "help":
        help()
        menu = input(colored("AutoMux >>> ","yellow"))
        if menu.strip() == "1" or menu.strip() == "01" or menu.strip() == "change":change()
        elif menu.strip() == "2" or menu.strip() == "02" or menu.strip() == "install":install_list()
        elif menu.strip() == "3" or menu.strip() == "03" or menu.strip() == "repair":repair_msf()
        elif menu.strip() == "4" or menu.strip() == "04" or menu.strip() == "trojan":msf_mm()
        elif menu.strip() == "5" or menu.strip() == "05" or menu.strip() == "update":update()
        elif menu.strip() == "0" or menu.strip() == "00" or menu.strip() == "exit":sys.exit()
        else:error()

    elif automux.strip() == "1" or automux.strip() == "01" or automux.strip() == "change":change()
    elif automux.strip() == "2" or automux.strip() == "02" or automux.strip() == "install":install_list()
    elif automux.strip() == "3" or automux.strip() == "03" or automux.strip() == "repair":repair_msf()
    elif automux.strip() == "4" or automux.strip() == "04" or automux.strip() == "trojan":msf_mm()
    elif automux.strip() == "5" or automux.strip() == "05" or automux.strip() == "update":update()
    elif automux.strip() == "0" or automux.strip() == "00" or automux.strip() == "exit":sys.exit()
    elif automux.strip() == "pwd":
        pwd = os.getcwd()
        print(pwd)
    else:error()  
 

def change():
    print(colored("\n请选择要更换的源:\n","blue"))
    print("    [01]  官方源")
    print("    [02]  清华大学源\n")
    print("    [00]  Bcak Menu\n")
    source = input(colored("AutoMux >>> ","yellow"))

    if source.strip() == "1" or source.strip()  == "01":gfy()
    elif source.strip() == "2" or source.strip()  == "02":qhd()
    elif source.strip()  == "0" or source.strip()  == "00":
        restart()
    else:error()  

def update():
    print("\n请选择更新方式:\n")
    print("    [01]  一键安装的更新")
    print("    [02]  克隆安装的更新\n")
    print("    [00]  Bcak Menu\n")
    up = input(colored("AutoMux >>> ","yellow"))

    if up.strip() == "0" or up.strip() == "00" or up.strip() == "exit":
        restart()
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

def install_list():
    print("\n    [01] 信息收集")
    print("    [02] 漏洞扫描")
    print("    [03] 压力测试")
    print("    [04] 密码攻击")
    print("    [05] 嗅探和欺骗")
    print("    [04] 利用工具")
    print("    [07] 其他\n")
    print("    [00] Bcak Menu\n")
    ilist = input(colored("AutoMux >>> ","yellow"))
    if ilist.strip() == "1" or ilist.strip() == "01":install.xxsj()
    elif ilist.strip() == "2" or ilist.strip() == "02":install.ldsm()
    elif ilist.strip() == "3" or ilist.strip() == "03":install.ylce()
    elif ilist.strip() == "4" or ilist.strip() == "04":install.mmgj()
    elif ilist.strip() == "5" or ilist.strip() == "05":install.xtqp()
    elif ilist.strip() == "6" or ilist.strip() == "06":install.lygj()
    elif ilist.strip() == "7" or ilist.strip() == "07":install.Other()
    elif ilist.strip() == "0" or ilist.strip() == "00":restart()


if __name__ == "__main__":
	main()
