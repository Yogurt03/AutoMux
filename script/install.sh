apt-get update
pkg install git python wget -y
git clone https://github.com/Bcap03/Muxtools.git $PREFIX/share/Muxtools
wget -P /bin https://raw.githubusercontent.com/Bcap03/Muxtools/master/script/muxtools && chmod 777 /bin/muxtools
echo "安装完成现在可以在任何地方输入'muxtools'来启动Muxtools了"

