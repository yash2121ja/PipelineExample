echo "Python code lint start"
cd ..
python3 -m pylint queue.py
echo -e "\e[1;31m This is red text \e[0m"
