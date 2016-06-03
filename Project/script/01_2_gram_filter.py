#!/usr/bin/python
# -*- coding: utf-8 -*-

# Takes the Google 2gram file, filters it (to keep what looks like a city)
# and saves the remaining lines in many files (openable by a text editor)
# In :
	# '../_data/googlebooks-eng-all-2gram-20120701-to'
# Out :
	# `nbLinesPerFile` line files in the directory `dirOut`
# Prerequisite:
	# Google 2gram "to" dataset

fileIn = '../_data/googlebooks-eng-all-2gram-20120701-to'
dirOut = "../_data/2gram-to/"

import csv
from time import *

nbLinesPerFile = 10000

def saveLines(lines, fileNb):
	if fileNb % 100 == 0:
		print(fileNb)
	with open(dirOut + "{0}.tsv".format(fileNb), 'w') as csvfile:
		writer = csv.writer(csvfile, delimiter='\t')
		for data in lines:
			writer.writerow(data)


time = process_time()

part1 = []
with open(fileIn, 'r') as csvfile:
	csvRows = csv.reader(csvfile, delimiter='\t')
	i=0
	fileNb = 0
	for csvRow in csvRows:
		currGram = csvRow[0] #.lower()
		if len(currGram) >= 4 and currGram[:3] == "to " and currGram[3].isalpha() and currGram[3].isupper():
			# print(csvRow)
			if i >= nbLinesPerFile:
				saveLines(part1, fileNb)
				part1 = []
				fileNb += 1
				i = 0
			else:
				i += 1
			part1.append(csvRow)

	saveLines(part1, fileNb)

print("Successfully read {0} lines in {1} second(s)".format((nbLinesPerFile * fileNb + len(part1)), int(process_time() - time)))
time = process_time()


# faire toward