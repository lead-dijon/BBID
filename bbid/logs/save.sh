for file in $(ls *.txt)
do
	mv $file ${file%.*}\_$(date +%Y-%m-%d).${file##*.}
	touch $file
	chmod 777 $file
done


