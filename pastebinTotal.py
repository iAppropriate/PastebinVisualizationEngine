"""
Background: This is run after a day's data has been collected. Three text files are read in,
one with IPs, one with Domains, and one with Email addresses. A tsv is outputed.


This script reads through a list of IPs, Domains, and Email addresses (Unvalidated; Basic Regex Only)
It outputs a row of the total number of IPs, Domains, and Email addresses to a running TSV file.
"""

from datetime import date, timedelta
import os.path 

# Get Yesterday's date
yesterday = date.today() - timedelta(1)
filename = (yesterday.strftime('%Y-%m-%d'))

# Enumurate number of entries
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# Find the length of yesterday's data files
ip = (file_len("/home/scraper/pastebin/ipMatch/" + filename))
domain = (file_len("/home/scraper/pastebin/domainMatch/" + filename))
email = (file_len("/home/scraper/pastebin/emailMatch/" + filename))

# if file doesn't exist, write header
if not os.path.isfile("/home/scraper/pastebin/overall/total/pastebinTotal.tsv"):
	with open("/home/scraper/pastebin/overall/total/pastebinTotal.tsv", "w") as createTotal:
		createTotal.write("Date\tIP\tDomain\tEmail\n")
	createTotal.close()

# Write entry for day
with open("/home/scraper/pastebin/overall/total/pastebinTotal.tsv", "a") as totalData:
	totalData.write(filename + "\t" + str(ip) + "\t" + str(domain) + "\t" + str(email) + "\n")
totalData.close()
