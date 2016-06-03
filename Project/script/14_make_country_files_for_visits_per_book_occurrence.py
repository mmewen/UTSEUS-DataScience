#!/usr/bin/python
# -*- coding: utf-8 -*-

# Turn country data to Excel tsv
# In :
	# "../_out/coutries_tourism_and_occurrences.json"
# Out :
	# "../_out/countries_visits/" folder, one [Country Code].tsv file for each country
# Prerequisite:
	# 13

import csv
import json

countriesFileIn = "../_out/coutries_tourism_and_occurrences.json"
dirOut = "../_out/countries_visits/"

def importCountries():
	ret = {}
	with open(countriesFileIn, 'r') as jsonfile:
		ret = json.load(jsonfile)
	print("Successfully imported {0} countries from {1} json file".format(len(ret), countriesFileIn))
	return ret

def saveFolders(countries):
	for country in countries:
		with open(dirOut + "{0}.tsv".format(countries[country]["Country Code"]), 'w') as csvfile:
			writer = csv.writer(csvfile, delimiter='\t')
			for x in xrange(1960,2016):
				pair = []
				try:
					pair.append(str(x))
					pair.append(countries[country]["occurrences"][str(x)])
					pair.append(countries[country]['International tourism'][str(x)])
					if pair[1]!=0 and pair[2]!=0:
						writer.writerow(pair)
				except Exception, e:
					pass
					# do nothing
	print("Successfully saved {0} countries data as tsv to {1} folder".format(len(countries), dirOut))

countries = importCountries()
saveFolders(countries)