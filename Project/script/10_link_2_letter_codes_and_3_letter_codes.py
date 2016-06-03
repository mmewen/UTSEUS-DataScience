#!/usr/bin/python
# -*- coding: utf-8 -*-

# Make a link between 2 letters Geonames country codes and 3 letters Worldbank 
# In :
	# "../_data/worldbank_countries.csv"
	#  "../_data/geonames_countries.csv"
# Out :
	# "../_out/2_to_3_country_codes.csv" file
# Prerequisite:
	# Just to have the datasets

import csv

worldbankFile = "../_data/worldbank_countries.csv"
geonamesFile = "../_data/geonames_countries.csv"
fileOut = "../_out/2_to_3_country_codes.csv"

twoLettersCodeToName = {}
nameToThreeLettersCode = {}

pairs = []
twoLettersErrors = []
threeLettersDone = []
threeLettersErrors = []

def importWorldbankFile():
	global nameToThreeLettersCode
	with open(worldbankFile,'rb') as csvfile:
		csvRows = csv.reader(csvfile, delimiter= '\t')
		next(csvRows)
		for csvRow in csvRows:
			nameToThreeLettersCode[csvRow[1].split(",")[0]] = csvRow[2]

def importGeonamesFile():
	global twoLettersCodeToName
	with open(geonamesFile,'rb') as csvfile:
		csvRows = csv.reader(csvfile, delimiter= '\t')
		next(csvRows)
		for csvRow in csvRows:
			twoLettersCodeToName[csvRow[3]] = csvRow[2]

def merge():
	global pairs, twoLettersErrors, threeLettersErrors
	for key in twoLettersCodeToName:
		try:
			threeLettersCode = nameToThreeLettersCode[twoLettersCodeToName[key]]
			threeLettersDone.append(threeLettersCode)
			pair = [key, threeLettersCode]
			pairs.append(pair)
		except Exception:
			twoLettersErrors.append([key, twoLettersCodeToName[key]])

	threeLettersErrors = [[nameToThreeLettersCode[x], x] for x in nameToThreeLettersCode if nameToThreeLettersCode[x] not in threeLettersDone]

def writeFile():
	print("Writing commented not to override manual changes. Save {0} somewhere else, uncomment the code and try again".format(fileOut))
	# with open(fileOut, 'w') as csvfile:
	# 	writer = csv.writer(csvfile, delimiter='\t')
	# 	for pair in pairs:
	# 		writer.writerow(pair)
	# 	for pair in sorted(twoLettersErrors, key=lambda error: error[0]):
	# 		writer.writerow(pair)
	# 	for pair in sorted(threeLettersErrors, key=lambda error: error[0]):
	# 		writer.writerow(pair)

importWorldbankFile()
importGeonamesFile()
merge()
writeFile()

print len(pairs)
print len(twoLettersErrors)
print len(threeLettersErrors)
# print("Successfully imported {0} cities from Geonames json file".format(len(geonamesCities)))