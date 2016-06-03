#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from sys import argv

cities = []
pathToCities = "../_out/dat_big_json/cities_1.json"

with open(pathToCities, 'r') as jsonfile:
	cities = json.load(jsonfile)
print("Loaded {0} cities".format(len(cities)))

# i = 0
# for key in cities:
# 	if i == 100:
# 		break
# 	print(key)

for city in argv[1:]:
	try:
		print(cities[city])
	except Exception:
		print("Not found")

answer = "Y"
while answer is not "":
	try:
		print(cities[answer])
	except Exception:
		print("Not found")

	print("Another city ?")
	answer = input()
	