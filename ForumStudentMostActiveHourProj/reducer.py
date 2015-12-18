#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the authorId, val is the added_at time's hour value
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

#dict for storing the hour value, count for number of times this hour value showed up
# dict will be reset to empty once all hour values for a particular key(authorId) have been processed
hrValCountDict = {}

def findMaxCountForActiveHour():
	maxVal = 0
	 
	for hrVal, count in hrValCountDict.iteritems():
		if maxVal < count:
			resultHr = hrVal
			maxVal = count

	return resultHr, maxVal

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHr = data_mapped

    # done processing all values of thisKey, so make the decisions and reset variables to move onto to next key
    if oldKey and oldKey != thisKey:
	activeHr, postCount = findMaxCountForActiveHour()
        print oldKey, "\t", activeHr, "\t", postCount
	
        oldKey = thisKey;
	hrValCountDict.clear()

    oldKey = thisKey

    hrValCountDict[thisHr] = 1 + hrValCountDict.get(thisHr, 0)

# calculations for the last key
if oldKey != None:
	activeHr, postCount = findMaxCountForActiveHour()
        print oldKey, "\t", activeHr, "\t", postCount



