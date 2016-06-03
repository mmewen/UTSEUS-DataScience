#!/usr/bin/python
# -*- coding: utf-8 -*-

# Makes a table aimed for a CartoDB map of occurrences in books in the specified timespan
# In :
	# merged-cities data files
	# geonames_cities.json
# Out :
	# ../_out/cartoDbCities/[begin]-[end].csv file
# Prerequisite:
	# 04, 05

import csv
import json
from os import walk

intervalBegin = 2000 # the year at which we begin to gather data (including this one)
intervalEnd = 2009 # the year at which we end to gather data (including this one)

geonamesCities = []
cartoDbCities = []
conj = "to"
dirIn = "../_out/2gram-"+conj+"-merged-cities/"
geonamesFile = '../_out/geonames_cities.json'
dirOut = "../_out/cartoDbCities/"

def importCities():
	global geonamesCities
	with open(geonamesFile, 'r') as jsonfile:
		geonamesCities = json.load(jsonfile)
	print("Successfully imported {0} cities from Geonames json file".format(len(geonamesCities)))

def saveCities():
	fileName = dirOut + "{0}-{1}.tsv".format(intervalBegin, intervalEnd)
	with open(fileName, 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter='\t')
		writer.writerow(['name', 'population', 'latitude', 'longitude', 'occurrences'])
		for data in cartoDbCities:
			writer.writerow(data)
	print("Successfully exported {0} cities to {1}".format(len(cartoDbCities), fileName))

def makeFile():
	global cartoDbCities
	for root, dirs, files in walk(dirIn):
		for filename in files:
			cityName = filename.split(".tsv")[0]
			with open(dirIn+filename, 'r') as csvfile:
				csvRows = csv.reader(csvfile, delimiter='\t')
				geonamesCity = geonamesCities[cityName]

				cartoDbCity = []
				cartoDbCity.append(cityName)
				cartoDbCity.append(geonamesCity["population"])
				cartoDbCity.append(geonamesCity["lat"])
				cartoDbCity.append(geonamesCity["long"])

				occurrences = 0
				for row in csvRows:
					if int(row[1]) >= intervalBegin and int(row[1]) <= intervalEnd:
						occurrences += int(row[2])
				cartoDbCity.append(occurrences)

				cartoDbCities.append(cartoDbCity)

importCities()
makeFile()
saveCities()

# And then we can put this in CartoDB