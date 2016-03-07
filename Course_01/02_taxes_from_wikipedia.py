#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

tax = {}

with open('./csv/US-taxes.csv', 'rb') as csvfile:
	csvRows = csv.reader(csvfile, delimiter=',')
	next(csvRows)
	for csvRow in csvRows:
		for cellIdx in xrange(len(csvRow)):
			csvRow[cellIdx] = csvRow[cellIdx].strip()

		csvRow[0] = csvRow[0].strip("()")
		# or
		# if 	csvRow[0][0] is '(':
		# 	csvRow[0] = csvRow[0][1:-1]

		if '[' in csvRow[0]:
			csvRow[0] = csvRow[0][0:-4]


		# if the cell #3 exists
		csvRow[2] = csvRow[2].strip().strip(" (max)").strip("+").strip("Dine-in")

		for cellIdx in xrange(len(csvRow)):
			csvRow[cellIdx] = csvRow[cellIdx].strip()

		# Ok cool, it's clean, let's remove the %
		for i in xrange(1, len(csvRow)):
			if "%" in csvRow[i]:
				csvRow[i] = csvRow[i][:-1]
			elif csvRow[i] is not "":
				print "Error at "
				print csvRow[i]

		state = csvRow[0]
		stdTax = csvRow[1]
		foodTax = csvRow[2]

		if foodTax is "":
			foodTax = stdTax
		
		tax[state] = float(foodTax)/100 if (foodTax is not "") else 0.0
		tax[state] = round(tax[state], 6)

		# print '|'.join(csvRow)



person=4
bill=100
state="Maine"

tip='good'
if tip=='good':
	bill += bill * 0.2
elif tip=='average':
	bill += bill * 0.15
elif tip=='bad':
	bill += bill * 0.1

bill += bill * tax[state]
bill = bill/person

print 'Each person should pay ' + str (bill)
