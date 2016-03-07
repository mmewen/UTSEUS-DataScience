#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv


stationsDico = {}
stationsArray = []

with open('./csv/data-gouv-gare-SNCF.csv', 'rU') as csvfile:
	csvRows = csv.reader(csvfile, delimiter=';')
	next(csvRows)
	for csvRow in csvRows:
		stationsDico[csvRow[1]] = ({
			'latitude': csvRow[3].replace(',', '.'),
			'longitude': csvRow[4].replace(',', '.'),
			})
		stationsArray.append([csvRow[1].replace(',', '.'), csvRow[3].replace(',', '.'), csvRow[4].replace(',', '.')])


# print stations

# with open("./csv/data-gouv-gare-SNCF-clean.json", 'wb') as file:
#     file.write(str(stationsDico))
#     # json.dump(stationsDico)

# OR

with open("./csv/data-gouv-gare-SNCF-clean.csv", 'wb') as csvfile:
	stationWriter = csv.writer(csvfile, delimiter=',')
	stationWriter.writerow(['name', 'latitude', 'longitude'])
	for data in stationsArray:
		stationWriter.writerow(data)
