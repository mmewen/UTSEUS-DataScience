#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from sys import argv

cities = []
pathToCounties = "../_out/coutries_tourism_and_occurences.json"

with open(pathToCounties, 'r') as jsonfile:
	cities = json.load(jsonfile)

for city in argv[1:]:
	try:
		print(cities[city])
	except Exception:
		print("Not found")
	