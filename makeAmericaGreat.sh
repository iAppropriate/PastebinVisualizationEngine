#script to grab only USA lines form input.csv
cat input.csv |grep "United States" >.tmpusa 
head -n 1 input.csv >usa.csv
cat .tmpusa >>usa.csv
rm .tmpusa
echo "Filtering input.csv into usa.csv"

cat input.csv|grep 'United States\|Russia\|China\|Brazil\|France\|United Kingdom\|India\|Australia\|Canada\|Germany\|South Africa' >.countries
head -n 1 input.csv >countries.csv
cat .countries >> countries.csv
rm .countries
echo "Filtering input.csv into countries.csv"
