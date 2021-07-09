echo "Python code lint start"
sh '''python3 -m pylint $(git ls-files '*.py')'''
echo -e "\e[1;31m This is red text \e[0m"
