## MTcore.py 是Muxtools实现功能文件
# -*- coding: utf-8 -*-

import os, sys
from time import sleep as timeout

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
    print("安装成功！2秒后重启AutoMux")
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
    os.system("apt-get update")
    print("更换成功！2秒后重启AutoMux")
    timeout(2)
    restart()

def gfy():
    print("更换官方源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://termux.org/packages/ stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt-get update")
    print("更换成功！2秒后重启AutoMux")
    timeout(2)
    restart()

def install_msf():
    print("安装msf中，请稍候...")
    os.system("pkg install unstable-repo -y")
    os.system("pkg install metasploit -y")
    okay()

def install_nmap():
    print("安装Nmap中，请稍候...")
    os.system("pkg install nmap -y")
    okay()

def repair_msf():
    print("修复msf数据库中，请稍候...")
    os.system("pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start")   
    print("修复成功！2秒后重启AutoMux")
    timeout(2)
    restart()

def install_sudo():
    print("安装sudo命令中，请稍候")
    os.system("git clone https://github.com/st42/termux-sudo.git")
    os.system("cd termux-sudo && cat sudo > $PREFIX/bin/sudo ")
    os.system("chmod 700 $PREFIX/bin/sudo")
    okay()

def upgrade_AutoMux():
    print("更新中...")
    os.system("git pull")
    timeout(2)
    restart()