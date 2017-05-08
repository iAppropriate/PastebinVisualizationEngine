#script to grab only USA lines form input.csv
cat input2.csv |grep "United States" >.tmpusa 
head -n 1 input.csv >usa.csv
cat .tmpusa >>usa.csv
rm .tmpusa
echo "cool things"
