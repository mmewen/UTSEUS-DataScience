#!/usr/bin/python
# -*- coding: utf-8 -*-

# Make a beautiful json from geonames csv
# In :
	# '../_data/Cities popularity/cities15000.txt'
# Out :
	# '../_out/geonames_cities.json'
# Prerequisite:
	# Geonames cities15000 dataset

import csv
import json

cities = {}
fileIn = '../_data/Cities popularity/cities15000.txt'
fileOut = '../_out/geonames_cities.json'

# Add loop to cities main names
with open(fileIn,'r') as csvfile:
	csvRows = csv.reader(csvfile, delimiter= '\t')
	for csvRow in csvRows:
		city = {}
		cityname = csvRow[2].split(" / ")[0]
		city["population"] = int(csvRow[14])
		city["country_2char"] = csvRow[8]
		city["lat"] = csvRow[4]
		city["long"] = csvRow[5]

		# We only keep the city with the biggest population (f*** Moscow in California)
		try:
			ret = cities[cityname]
			if ret["population"] < city["population"]:
				cities[cityname] = city
		except Exception:
			cities[cityname] = city
		


with open(fileOut,'w') as file:
	file.write(json.dumps(cities))


print("Successfully saved {0} cities from Geonames file".format(len(cities)))

