#!/usr/bin/python
# -*- coding: utf-8 -*-

# cef5dcb639f382ce8db12ddd1a38a44311bf4d96
from alchemyapi import AlchemyAPI
import json
import os
from os.path import join, getsize

alchemyapi = AlchemyAPI()

for root, dirs, files in os.walk('data/GOT5'):
    for name in files:
		print name
		with open(join(root, name),'r') as infile:
			text = infile.read()
			response = alchemyapi.entities('text', text, {'sentiment': 0})

			if response['status'] == 'OK':

				with open(join(root, name)[:-4]+'-entities.json','w') as outfile:
					json.dump(response,outfile)
			else:
				print 'problem with ',name