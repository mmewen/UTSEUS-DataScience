#!/usr/bin/python
# -*- coding: utf-8 -*-

# Transform city data to country data
# In :
	# "../_out/worldbank_tourism_data.json"
	# "../_out/dat_big_json/cities_1.json"
# Out :
	# "../_out/coutries_tourism_and_occurrences.json"
# Prerequisite:
	# 11, 12

import csv
import json
from os import walk

countries = {} # dico of countries -> data
cities = {} # dico of cities -> data
countriesFileIn =  "../_out/worldbank_tourism_data.json"
citiesFileIn = "../_out/dat_big_json/cities_1.json"

countriesFileOut = "../_out/coutries_tourism_and_occurrences.json"

def importCoutries():
	ret = {}
	with open(countriesFileIn, 'r') as jsonfile:
		ret = json.load(jsonfile)
	print("Successfully imported {0} cities from Worldbank json file".format(len(ret)))
	return ret

def importCities():
	ret = {}
	with open(citiesFileIn, 'r') as jsonfile:
		ret = json.load(jsonfile)
	print("Successfully imported {0} cities from our big occurences json file".format(len(ret)))
	return ret

def addCityOccurencesToCountry(cityOccurences, countryOccurrences):
	newCountryOccurrences = {}

	for year in countryOccurrences:
		newCountryOccurrences[year] = countryOccurrences[year]

	for year in cityOccurences:
		try:
			tmp = newCountryOccurrences[year] # test if the key exist
			# If we already have data for this year, make an addition
			newCountryOccurrences[year] += cityOccurences[year]
		except Exception:
			# Else, add a new entry to this dictionnary
			newCountryOccurrences[year] = cityOccurences[year]
	return newCountryOccurrences

def addCitiesToCountries():
	newCountries = {}
	# For each country
	for country in countries:
		newCountries[country] = countries[country]
		newCountries[country]["occurrences"] = {} # dico of year -> nb occurrences
		newCountries[country]["cities"] = [] # list of cities

		# print cities["Rawang"]
		# print newCountries[cities["Rawang"]["country_3char"]]
		# exit()

		# We find the cities in it
		for city in cities:
			if cities[city]["country_3char"] == newCountries[country]["Country Code"]:
				newCountries[country]["cities"].append(city)
				newCountries[country]["occurrences"] = addCityOccurencesToCountry(cities[city]["occurrences"], newCountries[country]["occurrences"])
				# !!!!!!!! are they all ints ?
		# print countries[country]
		# UPDATE COUNTRY IN COUNTRIES !!!!!!
	return newCountries

def saveCountries(countries):
	with open(countriesFileOut,'w') as file:
		file.write(json.dumps(countries))
	print("Successfully saved {0} countries to {1} file".format(len(countries), countriesFileOut))


countries = importCoutries()
cities = importCities()
countries = addCitiesToCountries()
saveCountries(countries)

# print(countries['FRA'])