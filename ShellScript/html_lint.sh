echo "Html code checking start"
sh '''python3 -m html-linter $(git ls-files '*.html')'''
echo "html code checked"
