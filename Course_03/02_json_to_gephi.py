#!/usr/bin/python
# -*- coding: utf-8 -*-

import networkx as nx
import json
import os

G=nx.Graph()

di = "GOT/Game of Thrones/data/"
for root, dirs, files in os.walk(di):
	for dirname in dirs:
		for root, dirs, files in os.walk(di+dirname):
			for filename in files:
				if 'entities' in filename and not "._" in filename:
					# print filename
					name = filename.split("-")[-2].title()
					# print name

					with open(di + dirname + "/" + filename, 'r') as jsonfile:
						entities = json.load(jsonfile)

					for entity in entities['entities']:
						# if "Person" in entity['type']:
						G.add_edge(name, entity['text'], weight = entity['count'])

# # G.add_node("spam")
# print(G.nodes())
# print(G.edges())
print(len(G.nodes()))
nx.write_gexf(G, "out.gexf")