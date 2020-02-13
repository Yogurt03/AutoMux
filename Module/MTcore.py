## MTcore.py 是Muxtools实现功能文件

import os, sys

Mt_banner =  """
 ______                              _      
|  ___ \             _              | |     
| | _ | |_   _ _   _| |_  ___   ___ | | ___ 
| || || | | | ( \ / )  _)/ _ \ / _ \| |/___)
| || || | |_| |) X (| |_| |_| | |_| | |___ |
|_||_||_|\____(_/ \_)\___)___/ \___/|_(___/ 

"""                                       

Mt_backmenu = """

    [99]    返回主菜单
    [00]    退出Muxtools

"""

def banner():
    print(Mt_banner)

def backmenu_option():
    print(Mt_backmenu)

def restart():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def install_lazymux():
    print("安装Lazymux中，请稍后...")
    os.system("git clone https://github.com/Gameye98/Lazymux.git $HOME/")

def qhd():
    print("更换清华源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://mirrors.tuna.tsinghua.edu.cn/termux stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt-get update")
def gfy():
    print("更换官方源中，请稍后...")
    os.system("rm -rf $PREFIX/etc/apt/sources.list")
    os.system('echo "deb https://termux.org/packages/ stable main" >$PREFIX/etc/apt/sources.list')
    os.system("apt-get update")

def install_msf():
    print("安装msf中，请稍候...")
    os.system("pkg install unstable-repo -y")
    os.system("pkg install metasploit -y")

def install_nmap():
    print("安装Nmap中，请稍候...")
    os.system("pkg install nmap -y")

def repair():
    print("修复msf数据库中，请稍候...")
    os.system("pg_ctl -D $PREFIX/var/lib/postgresql -l logfile start")
