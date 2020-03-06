##automux
# -*- coding: utf-8 -*-

import os, sys
from Module.AMcore import *
from time import sleep as timeout
from termcolor import *

def main():
    banner()
    print("    [01]  Change source")
    print("    [02]  Install list")
    print("    [03]  Msf Trojan")    
    print("    [04]  Repair Msfdb\n")  
    print("    [00]  Exit AutoMux\n")
    automux = input(colored("AutoMux >>> ","yellow"))

    if automux.strip() == "1" or automux.strip() == "01":
        print(colored("\n请选择要更换的源:\n","blue"))
        print("    [01]  官方源")
        print("    [02]  清华大学源\n")
        print("    [00]  Bcak Menu\n")
        source = input(colored("AutoMux >>> ","yellow"))

        if source.strip() == "1" or source.strip()  == "01":gfy()
        elif source.strip() == "2" or source.strip()  == "02":qhd()
        elif source.strip()  == "0" or source.strip()  == "00":restart()
        else:
            print(colored("\n输入错误，请重新输入！\n","red"))
            timeout(2)
            restart()   

    elif automux.strip() == "2" or automux.strip() == "02":
        print("\n    [01]  Nmap")
        print("    [02]  Hydra")
        print("    [03]  hping3" + colored(" < ","red")
        print("    [04]  sqlmap")
        print("    [05]  dnsmap")
        print("    [06]  Lazymux")
        print("    [07]  sslscan")
        print("    [08]  RED_HAWK")
        print("    [09]  WebCrack" + colored(" < ","red"))
        print("    [10]  Bettercap" + colored(" < ","red"))
        print("    [11]  Slowloris")
        print("    [12]  oh-my-zsh")
        print("    [13]  webdirscan"))
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
    elif automux.strip() == "3" or automux.strip() == "03":msf_mm()
    elif automux.strip() == "4" or automux.strip() == "04":repair_msf()
    elif automux.strip() == "0" or automux.strip() == "00" or automux.strip() == "exit":sys.exit()
    elif automux.strip() == "update":
        print(colored("更新中，请稍候...\n","green"))
        os.system("bash $PREFIX/share/AutoMux/update.sh")
        print(colored("\n更新完成AutoMux将在3秒后重启AutoMux\n","green"))
        timeout(3)
        restart()
    else:
        print(colored("\n输入错误，请重新输入！\n","red"))
        timeout(2)
        restart()

if __name__ == "__main__":
	main()
