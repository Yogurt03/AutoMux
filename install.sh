apt-get update
apt-get clean
pkg install git python wget -y
git clone https://github.com/Bcap03/Muxtools.git $PREFIX/share/Muxtools
echo "python $PREFIX/share/Muxtools/muxtools.py" >$PREFIX/bin/muxtools
chmod 777 $PREFIX/bin/muxtools
echo "安装完成现在可以在任何地方输入'muxtools'来启动Muxtools了"

