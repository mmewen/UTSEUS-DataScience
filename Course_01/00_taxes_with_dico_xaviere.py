person=4
bill=100
state="CA"
taxValues = {'CA':0.0725, 'NY': 0.04 , 'Rest': 0.06}
tip='good'

if tip=='good':
	bill += bill * 0.2
elif tip=='average':
	bill += bill * 0.15
elif tip=='bad':
	bill += bill * 0.1

bill += bill * taxValues[state]
bill= bill/person

print 'each person should pay ' + str (bill)


