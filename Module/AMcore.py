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

Tips.后面带有(Root)的需要手机有Root权限!!!

"""                                       

def banner():
    print(AM_banner)

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def okay():
    print(colored("\n安装成功！2秒后重启AutoMux\n","blue"))
    timeout(2)
    restart()

def install_lazymux():
    print("安装Lazymux中，请稍后...")
    os.system("git clone https://github.com/Gameye98/Lazymux.git")
    okay()

def qhd():
    print("更换清华源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt update")
    print("更换成功！2秒后重启AutoMux")
    timeout(2)
    restart()

def gfy():
    print("更换官方源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://termux.org/packages/ stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt  update")
    print("更换成功！2秒后重启AutoMux")
    timeout(2)
    restart()

def install_msf():
    print("安装msf中，请稍候...")
    os.system("apt install unstable-repo -y")
    os.system("apt install metasploit -y")
    okay()

def install_nmap():
    print("安装Nmap中，请稍候...")
    os.system("apt install nmap -y")
    okay()

def repair_msf():
    print("修复msf数据库中，请稍候...")
    os.system("pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start")   
    print("修复成功！2秒后重启AutoMux")
    timeout(2)
    restart()

def install_zsh():
    print("安装zsh中，请稍候...")
    os.system('sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh )"')
    okay()

def upgrade_AutoMux():
    print("更新中...")
    os.system("cd $PREFIX/share/AutoMux")
    os.system("git pull")
    os.system("cd $HOME")
    print("更新成功，2秒后重启AutoMux")
    timeout(2)
    restart()