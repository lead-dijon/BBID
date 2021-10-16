for file in $(ls *.txt)
do
	rm $file
	touch $file
	chmod 777 $file
done


