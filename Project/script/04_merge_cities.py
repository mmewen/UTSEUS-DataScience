#!/usr/bin/python
# -*- coding: utf-8 -*-

# Merge different orthographs of same city
# In :
	# "../_out/2gram-to-cities/" directory
# Out :
	# "../_out/2gram-to-merged-cities/" directory
# Prerequisite:
	# 03

import csv
import json
import time
import os
from shutil import copyfile
import re

conj = "to"
dirIn = "../_out/2gram-"+conj+"-cities/"
dirOut = "../_out/2gram-"+conj+"-merged-cities/"

def mergeFilesContents(city, listsToBeMerged):
	res = []
	i = []
	nbLists = range(len(listsToBeMerged))
	
	# We position us at the latest year
	# and we get the max year
	j = 0 # the studied year, which will decrease until all years have been studied
	for x in nbLists:
		i.append(len(listsToBeMerged[x])-1)
		if j<int(listsToBeMerged[x][i[x]][1]):
			j = int(listsToBeMerged[x][i[x]][1])

	# print(i)
	aListIsntFinished = True
	while aListIsntFinished and j>0:
		aListIsntFinished = False
		nbBooksThisYear = 0
		nbOccurrencesThisYear = 0

		for x in nbLists:
			if i[x] >= 0:
				aListIsntFinished = True

				# print(listsToBeMerged[x][i[x]])
				if j == int(listsToBeMerged[x][i[x]][1]):
					nbOccurrencesThisYear += int(listsToBeMerged[x][i[x]][2])
					nbBooksThisYear += int(listsToBeMerged[x][i[x]][3])
					i[x] -= 1

		if nbOccurrencesThisYear != 0:
			yearResult = [city, j, nbOccurrencesThisYear, nbBooksThisYear]
			res.append(yearResult)

		j -= 1

	res.reverse()

	return res

def saveMerge(city, content):
	with open(dirOut+"{0}.tsv".format(city), 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter='\t')
		for data in content:
			writer.writerow(data)


print("Is the folder {0} empty ?".format(dirOut))
answer = input()

if answer.lower() not in ['y', 'yes', 'o', 'oui']:
	print("Do it.")
	exit()


doubles = []
with open(dirIn + "doubles.txt", 'r') as f:
	lines = f.readlines()
	for line in lines:
		doubles.append(line.strip())

# First merge cities with many names
for root, dirs, files in os.walk(dirIn):

	# For every city that has multiple names
	for city in doubles:
		cityRowsOfFiles = [] # city data from every file (array of array)

		# Get all the files that refers to this city (same filename beginning, with a number afterwards)
		cityFiles = [x for x in files if city in x]

		# if city == "Washington, D.C.":
		# 	print(cityFiles)

		# For each file of the city
		for cityFile in cityFiles:
			# Get the file content
			cityRowsOfFile = [] # array of lines, one for each file
			with open(dirIn+cityFile, 'r') as csvfile:
				csvRows = csv.reader(csvfile, delimiter='\t')

				for row in csvRows:
					cityRowsOfFile.append(row)
			cityRowsOfFiles.append(cityRowsOfFile)

		# if city == "Washington, D.C.":
		# 	print(len(cityRowsOfFiles))
		# 	for t in cityRowsOfFiles:
		# 		print(len(t))
		merge = mergeFilesContents(city, cityRowsOfFiles)

		# if city == "Washington, D.C.":
		# 	print(len(merge))

		saveMerge(city, merge)


isADouble = re.compile(r".*-[0-9]+\.tsv$")
# Then copy cities with only 1 name (= 1 file)
for root, dirs, files in os.walk(dirIn):
	for fileName in files:
		# print("=={0}".format(fileName))
		# print(fileName.split(".")[0] not in doubles)
		itIsNOTADouble = isADouble.match(fileName) == None
		# print(itIsNOTADouble)
		# print(fileName.split(".")[0] not in doubles and itIsNOTADouble)
		# input()
		if fileName.split(".tsv")[0] not in doubles and itIsNOTADouble and fileName != "doubles.txt":
			copyfile(dirIn + fileName, dirOut + fileName)