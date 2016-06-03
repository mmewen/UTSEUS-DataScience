#!/usr/bin/python
# -*- coding: utf-8 -*-

# Transform Worldbank data to json
# In :
	# "../_data/data.worldbank/API_ST.INT.ARVL_DS2_en_csv_v2.csv"
	# "../_out/2_to_3_country_codes.csv"
# Out :
	# "../_out/worldbank_tourism_data.json" file
# Prerequisite:
	# 10 and the Worldbank dataset

import csv
import json

worldBankData = "../_data/data.worldbank/API_ST.INT.ARVL_DS2_en_csv_v2.csv"
countryCodeFile = "../_out/2_to_3_country_codes.csv"
countriesFileOut =  "../_out/worldbank_tourism_data.json"

countryCode2To3 = {}
countriesDico = {}
citiesDico = {}

def importCountryCodeFile():
	ret = []
	with open(countryCodeFile,'r') as csvfile:
		csvRows = csv.reader(csvfile, delimiter= '\t')
		for csvRow in csvRows:
			ret.append(csvRow)
	return ret

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def importWorldBankCountriesFile():
	ret = {} # dico of 3 letters country code key and the related data
	with open(worldBankData,'r') as csvfile:
		csvRows = csv.reader(csvfile, delimiter= ',')
		next(csvRows)
		first = True
		head = []
		for csvRow in csvRows:
			csvRowCleaned = []
			for cell in csvRow:
				csvRowCleaned.append(cell) #cell[1:-1])

			if first:
				head = csvRowCleaned
				first = False
			else:
				ret[csvRowCleaned[1]] = {}

				i = 0
				ret[csvRowCleaned[1]]["International tourism"] = {}
				for header in head:
					if isInt(header): # this is a year
						if csvRowCleaned[head.index(header)] is "":
							csvRowCleaned[head.index(header)] = "0"
						ret[csvRowCleaned[1]]["International tourism"][int(header)] = int(csvRowCleaned[head.index(header)].split(".")[0])
					else: # it's another data
						ret[csvRowCleaned[1]][header] = csvRowCleaned[head.index(header)]
					# Treat occurrences !
					# Be carefull of years without data
					# store keys and values as int
	return ret

def saveCountriesDico(countries):
	with open(countriesFileOut,'w') as file:
		file.write(json.dumps(countries))

countryCode2To3 = importCountryCodeFile()
countriesDico = importWorldBankCountriesFile()
saveCountriesDico(countriesDico)