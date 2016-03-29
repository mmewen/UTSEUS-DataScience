#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml.html.soupparser import fromstring
from lxml.etree import tostring
from characters import characters
import requests
import time
import json

baseUrl = 'http://awoiaf.westeros.org'
# r = requests.get(baseUrl + '/index.php/List_of_Characters')
# tree = fromstring(r.text)
# charactersLink = []
# characters = tree.xpath('//div[@id="bodyContent"]//li/a')
# for character in characters:
# 	try:
# 		charactersLink.append(character.get('href'))
# 	except:
# 		pass
# print charactersLink


characterList = []
for character in characters:
	r = requests.get(baseUrl + character)
	tree = fromstring(r.text)
	infobox = tree.xpath('//table[@class="infobox infobox-body"]')
	if len(infobox) == 0:
		# print 'not found for characterLink'
		continue
	myCharacter = {}
	name = infobox[0][0].text_content().strip()
	if 'Hodor' in character:
		print 'this hodor, skip it'
		continue
	myCharacter['name'] = name
	infos = infobox[0].xpath('.//tr')
	for info in infos:
		if info[0].tag == 'th':
			try:
				myCharacter[info[0].text_content().strip().lower()] = info[1].text_content().strip()
			except IndexError:
				print 'problem with name ',character

		
	characterList.append(myCharacter)
	time.sleep(1.0)

print json.dumps(characterList)