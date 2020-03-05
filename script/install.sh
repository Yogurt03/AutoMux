apt update
apt install git python -y
pip install termcolor
git clone https://github.com/Bcap03/AutoMux.git $PREFIX/share/AutoMux
echo "python $PREFIX/share/AutoMux/automux.py" >$PREFIX/bin/automux
chmod 777 $PREFIX/bin/automux
echo "bash $PREFIX/share/AutoMux/update.sh" >$PREFIX/bin/update-AutoMux
chmod 777 $PREFIX/bin/aupdate-AutoMux
echo -e "\n\033[31m安装完成，请输入'automux'来启动AutoMux。\033[0m\n"