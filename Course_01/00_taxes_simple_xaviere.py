person=4
bill=100
tip=15.5
tax=4

total=(bill+tip/100*bill)
total=(total+total*tax/100)/person
print "the price per person is " + str (total) + " $"

