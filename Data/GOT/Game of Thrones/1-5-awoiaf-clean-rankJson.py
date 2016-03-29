#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import re

p = re.compile('([a-z][A-Z])')

with open('data/charactersNormalize.json') as jsonFile:
	characters = json.load(jsonFile)

for character in characters:
	if character['alias'] <> None:
		print '[' + character['name'].encode('utf-8') + ']: ' + character['alias'].encode('utf8')
		