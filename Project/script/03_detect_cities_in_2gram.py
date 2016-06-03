#!/usr/bin/python
# -*- coding: utf-8 -*-

# Use Python 3 !
# Filter 2gram files to keep cities that really exist
# In :
	# "../_data/2gram-to/" directory
	#  "../_out/inverted_cities.json"
# Out :
	# "../_out/2gram-to-cities/" directory
# Prerequisite:
	# 01, 02

import csv
import json
import time
import os

conj = "to"
dirIn = "../_data/2gram-"+conj+"/"
dirOut = "../_out/2gram-"+conj+"-cities/"
rowWord = "" # name of the current row minus the "conj"
prevRowWord = "" # name of the current row minus the "conj"
currentCityName = ""
savingLines = False

cities = []
pathToCities = "../_out/inverted_cities.json"

cityOccurances = [] # result
cityCount = 0

doubles = {} # list of the doublons

def importCities():
	global cities
	with open(pathToCities, 'r') as jsonfile:
		cities = json.load(jsonfile)

def getOriginalName(name):
	if cities == []:
		importCities()
	ret = ""

	try:
		ret = cities[name]
	except Exception:
		return ""

	return ret

def saveLine(originalName, csvRow):
	global cityOccurances
	csvRow[0] = originalName
	cityOccurances.append(csvRow)

def saveCity(cityName):
	# print(cityName)
	global cityOccurances, cityCount, doubles

	copy = 0
	fileName = cityName
	while os.path.isfile(dirOut + "{0}.tsv".format(fileName)):
		doubles[cityName] = True
		copy += 1
		fileName = cityName + "-" + str(copy)

	with open(dirOut + "{0}.tsv".format(fileName), 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter='\t')
		for data in cityOccurances:
			writer.writerow(data)
	cityCount += 1
	cityOccurances = []

print("Is the folder {0} empty ?".format(dirOut))
answer = input()

if answer.lower() not in ['y', 'yes', 'o', 'oui']:
	print("Do it.")
	exit()

timer = time.process_time()

i = 0
for root, dirs, files in os.walk(dirIn):
	for filename in files:
		if i%100 == 0:
			print(i)
		i += 1
		# print(dirIn+filename)
		with open(dirIn+filename, 'r') as csvfile:
			csvRows = csv.reader(csvfile, delimiter='\t')
			# next(csvRows)

			for csvRow in csvRows:
				# get rowWord
				rowWord = csvRow[0][len(conj) + 1:]

				# if the row word has changed
				if rowWord != prevRowWord:

					# save it
					if savingLines:
						saveCity(originalName)
					prevRowWord = rowWord
					originalName = getOriginalName(rowWord)

					# if it's not a real city
					if originalName is "":
						savingLines = False
					else:
						# it's a real city, save the next lines !
						# print(currentCityName, " -> ", rowWord," . ", originalName)
						# t = input()
						currentCityName = originalName
						savingLines = True
				else:
					# the row word is the same as the previous line
					if savingLines:
						saveLine(rowWord, csvRow)

with open(dirOut + "doubles.txt", 'w') as f:
	for key in doubles:
		f.write(key + "\n")


print("Successfully found {0} cities in {1} second(s)".format(cityCount, int(time.process_time() - timer)))
timer = time.process_time()