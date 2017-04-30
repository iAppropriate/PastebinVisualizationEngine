"""
Background: This is run after a day's data has been collected. A .txt files is taken in and a csv is outputed.


This script reads through a list of supposed IP addresses (based on simple regex)
removes duplicates entries, validates IP addresses. It is at this point that a GeoIP Serivce is queried 
with the publicly routable addresses. Reponses are sent as json and stored in a csv file.
"""

from pprint import pprint
from datetime import date, timedelta
import pycurl
import json
import io
import csv
import os
import requests

# Get Yesterday's date
yesterday = date.today() - timedelta(1)
filename = (yesterday.strftime('%Y-%m-%d'))

# Create Unique list
os.system("sort " + "/home/scraper/pastebin/ipMatch/" + filename + " | uniq > " + "/home/scraper/pastebin/ipMatch/" + filename + "_sort")

# Prepare to read unique values only
filename = filename + "_sort"

def jsonScraper():

	# Read in unique values
	with open("/home/scraper/pastebin/ipMatch/" + filename, "r") as ipReader:

		# Zero out previous IP Address
		prevIP = ""

		for line in ipReader:
			writeJson = io.BytesIO()
			ip = line.split(" ")[0]
			ipCheck = ip.split(".")
			fail = 0

			# If duplicate address is found
			if prevIP.strip() == ip.strip():
				continue

			# Invalid if first octet contains leading 0
			if (int(ipCheck[0][0]) == 0) and len(ipCheck[0]) > 1:
				continue

			# Invalid if loopback address
			if (int(ipCheck[0]) == 127 and ((int(ipCheck[1]) >= 16 or int(ipCheck[1]) <= 31))):
				continue

			# Invalid if Class A address
			if (int(ipCheck[0]) == 10) or (int(ipCheck[0]) == 0) or (int(ipCheck[0]) == 255):
				continue
			
			# Invalid if APIPA address
			if (int(ipCheck[0]) == 169) and (int(ipCheck[1]) == 254):
				continue

			# Invalid if Class C address
			if (int(ipCheck[0]) == 192) and (int(ipCheck[1]) == 168):
				continue

			# Fail if octet is greater than 255 or less than 0.
			for octet in ipCheck:
				if int(octet) > 255:
					fail = 1
					break
				elif int(octet) < 0:
					fail = 1
					break

			if fail == 1:
				continue

			
			url = "https://freegeoip.net/json/" + str(ip.strip())
			resp = requests.get(url)
			data = resp.json()
			pprint(data)

			# If "country_code" and "time_zone" are missing, the IP is invalid; do not write
			if not data["country_code"] and not data["time_zone"]:
				continue

			# Arrange csv row
			row = [data["ip"], data["country_code"], data["country_name"], data["latitude"], data["longitude"], data["metro_code"], data["region_code"], data["region_name"], data["city"], data["time_zone"], data["zip_code"]]
			prevIP = data["ip"]
			
			# Create csv if it doesn't exist
			if not os.path.isfile("/home/scraper/pastebin/CSVs/" + filename[:-5] + ".csv"):	
				with open("/home/scraper/pastebin/CSVs/" + filename[:-5] + ".csv", "w", newline="") as createCSV:
				
					# Write header
					writeHeader = csv.writer(createCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
					header = ("ip", "countrycode", "name", "latitude", "longitude", "metrocode", "regioncode", "regionname", "city", "timezone", "zipcode")

					writeHeader.writerow(header)

				createCSV.close()
			
			with open("/home/scraper/pastebin/CSVs/" + filename[:-5] + ".csv", "a", newline="") as csvFile:
			
				csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

				# Write row
				csvWriter.writerow(row)
			
			csvFile.close()

	ipReader.close()

jsonScraper()
