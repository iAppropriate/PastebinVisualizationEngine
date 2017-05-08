# The Pastebin Visualization Engine

Core Contributors:
Lucas Christian (lxc6101@rit.edu)
Sam Merchant (shm7372@rit.edu)
Akshit Jain (avj2668@rit.edu)

## Summary:
Our goal is to make a product that can scrape posts to pastebin for contents of our chosing and visualize the information in a useful format. We approached this task in two parts. First we grab files from pastebin and form the data into a csv or tsv for convinience. Next we read this data into a format that matches the appropriate visualization. 

## Back-end:

On the backend, there is a script that seeks through each Pastebin post looking for data that matches a regex; this might include: IP address, domain name, or email address. If a string matches the regex it is added to a list of homogenous data types such as a list of other IP addresses collected from the current day. At the start of every day, the previous days data is validated; In the case of IP addresses, each octet is checked for validity and non-routable addresses are excluded. It is at this point, we use a Geolocation service on each unique IP. Each response is sent to are server and is in turn written to a CSV file which is later used by our front end visualization tool. Running concurrently to the IP Validation script, are two additional scripts, they are enumerating the total number of regex matches by category and the unique number of regex matches by category, respectively. Each of these values are appended to a row in separate TSV files.

## Front-end:

The CSV and the two TSVs are passed to the front-end where these simplified data sets can be displayed on one of our select visualizations. Our Visualizations include: GPS Coordinates by Unique IP Address displayed on a world map, GPS Coordinates by Unique IP Address displayed on a US map,  a bar graph displaying total IP addresses across 10 select country codes, a line graph displaying unique values on a range of dates, or total values on a range of dates (this includes IP addresses, Domain names, and Email addresses).

