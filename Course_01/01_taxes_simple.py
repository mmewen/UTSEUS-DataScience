#!/usr/bin/python
# -*- coding: utf-8 -*-

print("Ok, let's see what 4 people need to pay when the bill is 100$")

bill = 100
nbPeople = 4
tip = 19 # %
tax = 4 # %

total = (bill * (tip/100.0 + 1)) * (tax/100.0 + 1)

print("Each person has to pay " + (`total / nbPeople)` + "$")