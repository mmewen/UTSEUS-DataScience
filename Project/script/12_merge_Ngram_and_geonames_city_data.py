#!/usr/bin/python
# -*- coding: utf-8 -*-

# Make a big json file with all the data we have for each city
# In :
	# "../_out/2gram-to-merged-cities/"
	# '../_out/geonames_cities.json'
	# "../_out/2_to_3_country_codes.csv"
# Out :
	# "../_out/dat_big_json/cities_1.json"
# Prerequisite:
	# 04, 05, 10

import csv
import json
from os import walk

geonamesCities = {} # dico of cities -> data ()
ngramCities = {}
countryCodes = {}

conj = "to"
dirIn = "../_out/2gram-"+conj+"-merged-cities/"
geonamesFile = '../_out/geonames_cities.json'
twoTo3CoutryCodesFile = "../_out/2_to_3_country_codes.csv"

fileOut = "../_out/dat_big_json/cities_1.json"

def importCountryCodes():
	ret = {}
	with open(twoTo3CoutryCodesFile, 'r') as csvfile:
		csvRows = csv.reader(csvfile, delimiter='\t')
		for row in csvRows:
			ret[row[0]] = row[1]
	print("Successfully imported {0} country codes from tsv file".format(len(ret)))
	return ret

def importGeonamesCities():
	ret = {}
	with open(geonamesFile, 'r') as jsonfile:
		ret = json.load(jsonfile)
	print("Successfully imported {0} cities from Geonames json file".format(len(ret)))
	return ret

def importNgramCities():
	ret = {}
	for root, dirs, files in walk(dirIn):
		for filename in files:
			cityName = filename.split(".tsv")[0]
			if cityName == 'doubles.txt':
				continue

			with open(dirIn+filename, 'r') as csvfile:
				csvRows = csv.reader(csvfile, delimiter='\t')
				geonamesCity = geonamesCities[cityName]
				
				ret[cityName] = {
					"population": geonamesCity["population"],
					"lat": geonamesCity["lat"],
					"long": geonamesCity["long"]
				}

				occurrences = 0
				ret[cityName]["totalOccurrences"] = 0
				ret[cityName]["occurrences"] = {}
				for row in csvRows:
					year = int(row[1])
					ret[cityName]["occurrences"][year] = int(row[2]) # dic of year -> value
					ret[cityName]["totalOccurrences"] += int(row[2]) # sum of occurrences for all time
	print("Successfully imported {0} cities from Ngrams files".format(len(ret)))
	return ret

def addGeonamesDataToNgramCities(geonames, ngram):
	ret = {}

	for key in ngram:
		ret[key] = ngram[key]
		for attribute in geonames[key]:
			ret[key][attribute] = geonames[key][attribute]
		ret[key]["country_3char"] = countryCodes[ret[key]["country_2char"]]

	return ret

def saveCities(cities):
	with open(fileOut,'w') as file:
		file.write(json.dumps(cities))
	print("Successfully saved {0} cities to {1} file".format(len(cities), fileOut))
		
countryCodes = importCountryCodes()
geonamesCities = importGeonamesCities()
ngramCities = importNgramCities()
# for key in ngramCities:
# 	print(key)
# 	print(ngramCities[key])
# 	break
merge = addGeonamesDataToNgramCities(geonamesCities, ngramCities)
# for key in merge:
# 	print(key)
# 	print(merge[key])
# 	break
saveCities(merge)
# makeFile()
# saveCities()
# print("Got {0} cities in {1}".format(countries))
