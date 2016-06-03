#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from sys import argv

cities = []
pathToCities = "../_out/inverted_cities.json"

with open(pathToCities, 'r') as jsonfile:
	cities = json.load(jsonfile)

for city in argv[1:]:
	try:
		print(cities[city])
	except Exception:
		print("Not found")
	