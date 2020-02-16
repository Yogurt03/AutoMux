apt-get update
clear
echo "安装依赖中..."
pkg install git python -y
pip install termcolor
git clone https://github.com/Bcap03/AutoMux.git $PREFIX/share/AutoMux
echo "python $PREFIX/share/AutoMux/automux.py" >$PREFIX/bin/automux
chmod 777 $PREFIX/bin/automux
echo "安装完成现在可以在任何地方输入'muxtools'来启动Muxtools了"