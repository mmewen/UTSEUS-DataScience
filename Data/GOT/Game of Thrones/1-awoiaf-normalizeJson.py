#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

with open('data/characters.json') as fp:
	raw_json = fp.read()

raw_characters = json.loads(raw_json)
#put an id
#verify is there is a name
#remove organizations
#add hodor
#check aliases and create array with a split
#remove every [] from each field
#give a score to each given their importance (try long name first)

final_characters = []
GOT1_title = 'a game of thrones'
GOT2_title = 'a clash of kings'
GOT3_title = 'a storm of swords'
GOT4_title = 'a feast for crows'
GOT5_title = 'a dance with dragons'

for character in raw_characters:
	if character.get('location') <> None or character.get('organization') <> None or character.get('region') <> None or character.get('name') is None:
		continue

	myCharacter = {}
	myCharacter['name'] = character.get('name')
	
	if character.get('alias') <> None:
		myCharacter['alias'] = character.get('alias').encode('utf-8')
	else:
		myCharacter['alias'] = None
	if character.get('book(s)') <> None:
		myCharacter['books'] = []
		if GOT1_title in character.get('book(s)').lower():
			myCharacter['books'].append(GOT1_title)
		if GOT2_title in character.get('book(s)').lower():
			myCharacter['books'].append(GOT2_title)
		if GOT3_title in character.get('book(s)').lower():
			myCharacter['books'].append(GOT3_title)
		if GOT4_title in character.get('book(s)').lower():
			myCharacter['books'].append(GOT4_title)
		if GOT5_title in character.get('book(s)').lower():
			myCharacter['books'].append(GOT5_title)
		if len(myCharacter['books'])==0:
			continue

	myCharacter['allegiance'] = character.get('allegiance')
	final_characters.append(myCharacter)

# we use alchemy API for each chapter of the book 
print json.dumps(final_characters)