echo -e "\033[31m更新AutoMux中请稍候...\033[0m"
$PREFIX
cd /share/AutoMux
git stash
git pull
echo -e "\033[31m更新完成，请输入'automux'开启AutoMux\033[0m"
