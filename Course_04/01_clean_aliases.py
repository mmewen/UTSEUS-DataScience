#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import json
import os
import re

data = []
dataCleaned = []

# reLowerUpper = re.compile("([a-z])([A-Z])")

with open('../Data/GOT/Game of Thrones/data/charactersNormalize.json', 'r') as jsonfile:
	data = json.load(jsonfile)
	for d in data:

		if d['alias'] is None:
			continue

		d['alias'] = d['alias'].encode("utf-8")
		# print "  " + d['alias']

		i = 0

		while i < len(d['alias']) - 1:
			if  d['alias'][i] is "[" and (i + 2) < len(d['alias']):
				if i+4 > len(d['alias']):
					d['alias'] = d['alias'][:i]
				else:
					d['alias'] = d['alias'][:i] + "|" + d['alias'][i+3:]
			elif d['alias'][i] is ")" and d['alias'][i+1].isupper():
				d['alias'] = d['alias'][:i] + "|" + d['alias'][i+1:]
			elif d['alias'][i] is " " and d['alias'][i+1] is "(" and d['alias'][i+2] is not "I":
				d['alias'] = d['alias'][:i+1] + "|" + d['alias'][i+2:]
			elif d['alias'][i].islower() and d['alias'][i+1].isupper():
				d['alias'] = d['alias'][:i+1] + "|" + d['alias'][i+1:]
			i += 1

		d['alias'] = d['alias'].replace('"', '')
		d['alias'] = d['alias'].replace('| |', '|')
		d['alias'] = d['alias'].replace('possible|', '')
		d['alias'] = d['alias'].replace('/', '|')
		if "|" in d['alias']:
			d['alias'] = d['alias'].split("|")
		else:
			d['alias'] = d['alias'].split("  ")

		tmp = []

		for i in range(0, len(d['alias'])):
			if d['alias'][i] in [" ", ""]:
				continue

			if d['alias'][i][-1] is ")":
				d['alias'][i] = d['alias'][i][:-1]

			d['alias'][i] = d['alias'][i].strip()

			tmp.append(d['alias'][i])

		d["alias"] = tmp

		print d['alias']

		dataCleaned.append(d)



with open('../Data/GOT/Game of Thrones/data/charactersNormalize2.json', 'wb') as f:
	f.write(json.dumps(dataCleaned))


# print(data)




# G=nx.Graph()

# di = "GOT/Game of Thrones/data/charactersNormalize.json"
# for root, dirs, files in os.walk(di):
# 	for dirname in dirs:
# 		for root, dirs, files in os.walk(di+dirname):
# 			for filename in files:
# 				if 'entities' in filename and not "._" in filename:
# 					# print filename
# 					name = filename.split("-")[-2].title()
# 					# print name

# 					with open(di + dirname + "/" + filename, 'r') as jsonfile:
# 						entities = json.load(jsonfile)

# 					for entity in entities['entities']:
# 						# if "Person" in entity['type']:
# 						G.add_edge(name, entity['text'], weight = entity['count'])

# # # G.add_node("spam")
# # print(G.nodes())
# # print(G.edges())
# print(len(G.nodes()))
# nx.write_gexf(G, "out.gexf")

