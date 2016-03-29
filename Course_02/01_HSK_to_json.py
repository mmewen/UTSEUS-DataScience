#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import json

voc = []

with open('./csv/HSK Official With Definitions 2012 L1.tsv', 'rb') as csvfile:
	csvRows = csv.reader(csvfile, delimiter='\t')
	next(csvRows)
	for csvRow in csvRows:
		voc.append({
			"chinese": csvRow[0],
			"pinyin": csvRow[3],
			"english": csvRow[4].split("; ")
			})


with open('./json/hsk1.json', 'wb') as f:
	f.write(json.dumps(voc))


