"""
Background: This is run after a day's data has been collected. Three text files are read in,
one with IPs, one with Domains, and one with Email addresses. A tsv is outputed.


This script reads through a list of IPs, Domains, and Email addresses (Unvalidated; Basic Regex Only)
It outputs a row of the unique number of IPs, Domains, and Email addresses to a running TSV file.
"""

from pprint import pprint
from datetime import date, timedelta
import os.path

# Get Yesterday's date
yesterday = date.today() - timedelta(1)
filename = (yesterday.strftime('%Y-%m-%d'))

# Create file with unique values
os.system("sort " + "/home/scraper/pastebin/ipMatch/" + filename + " | uniq > " + "/home/scraper/pastebin/overall/unique/" + filename + "_ip")
os.system("sort " + "/home/scraper/pastebin/domainMatch/" + filename + " | uniq > " + "/home/scraper/pastebin/overall/unique/" + filename + "_domain")
os.system("sort " + "/home/scraper/pastebin/emailMatch/" + filename + " | uniq > " + "/home/scraper/pastebin/overall/unique/" + filename + "_email")

# Enumerate file lengths
def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i + 1

# Find the length of yesterday's data files
ip = (file_len("/home/scraper/pastebin/overall/unique/" + filename + "_ip"))
domain = (file_len("/home/scraper/pastebin/overall/unique/" + filename + "_domain"))
email = (file_len("/home/scraper/pastebin/overall/unique/" + filename + "_email"))

# if file doesn't exist, write header
if not os.path.isfile("/home/scraper/pastebin/overall/total/pastebinUnique.tsv"):
	with open("/home/scraper/pastebin/overall/total/pastebinUnique.tsv", "w") as createUnique:
		createUnique.write("Date\tIP\tDomain\tEmail\n")
	createUnique.close()

# Write entry for day
with open("/home/scraper/pastebin/overall/total/pastebinUnique.tsv", "a") as uniqueData:
	uniqueData.write(filename + "\t" + str(ip) + "\t" + str(domain) + "\t" + str(email) + "\n")
uniqueData.close()
