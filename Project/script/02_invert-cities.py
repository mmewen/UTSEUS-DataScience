#!/usr/bin/python
# -*- coding: utf-8 -*-

# Takes the Geonames cities and transform the file to easily find
# the regular name of a city from an alias
# In :
	# '../_data/Cities popularity/cities15000.txt'
# Out :
	# '../_out/inverted_cities.json'
# Prerequisite:
	# Geonames cities15000 dataset

import csv
import json

dico = {}
fileIn = '../_data/Cities popularity/cities15000.txt'
fileOut = '../_out/inverted_cities.json'
filterUnder = 100000

# Add loop to cities main names
with open(fileIn,'rb') as csvfile:
	csvRows = csv.reader(csvfile, delimiter= '\t')
	for csvRow in csvRows:
		pop = int(csvRow[14])
		if pop > filterUnder:
			dico[csvRow[2]] = csvRow[2].split(" / ")[0]

nbCities = len(dico)

with open(fileIn,'rb') as csvfile:
	csvRows = csv.reader(csvfile, delimiter= '\t')
	for csvRow in csvRows:
		pop = int(csvRow[14])
		if pop > filterUnder:
			noms = csvRow[3].split(",")
			for nom in noms:
				try:
					tmp = dico[nom] # try to get the city
				except Exception:
					# if it doesn't already exist, add it
					dico[nom]= csvRow[2].split(" / ")[0]

with open(fileOut,'w') as file:
	file.write(json.dumps(dico))

print("Successfully read {0} aliases of {1} cities with population above {2}".format(len(dico) - nbCities, nbCities, filterUnder))
