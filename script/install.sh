apt-get update
pkg install git python wget
git clone https://github.com/Bcap03/Muxtools.git $PREFIX/share/
wget -P /bin https://raw.githubusercontent.com/Geeks-alliance/Auto-Kali/master/scrips/auto-kali && chmod 777 /bin/auto-kaliecho "安装完成现在可以在任何地方输入'muxtools'来启动Muxtools了"

