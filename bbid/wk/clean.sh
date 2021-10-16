find . -name "*.zip" -o -name "*.txt" -ctime 0 -exec /bin/rm -f '{}' ';'
