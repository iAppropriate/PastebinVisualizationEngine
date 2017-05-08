#File to load specific day into input.csv
file=$1
fileext=${file##*.}

#Checking file extension
if [ $fileext == "csv" ];
then
	echo "Loading $file"
	cp $file input.csv
	echo "Copying $file to input.csv"
	bash makeAmericaGreat.sh #running script to update usa.csv and countries.csv
else
	echo "Incorrect file type!" #print error message
fi
