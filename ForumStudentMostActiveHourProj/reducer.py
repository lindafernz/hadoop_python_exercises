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
	outHrVal = {}
	 
	for hrVal, count in hrValCountDict.iteritems():
		if maxVal < count:
			maxVal = count
	
	# now that we have the max value between all hours in the student's active hour list
	# populate the list for all the hour values when the count is that max value
	for hrVal, count in hrValCountDict.iteritems():
		if maxVal == count:
			outHrVal[hrVal] = count
	

	return outHrVal

def printResults(authId, hrCountDict):
	for activeHr, postCount in hrCountDict.iteritems():
	        print authId, "\t", activeHr, "\t", postCount
		

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHr = data_mapped

    # done processing all values of thisKey, so make the decisions and reset variables to move onto to next key
    if oldKey and oldKey != thisKey:
	activeHrCountDict = findMaxCountForActiveHour()
        #print oldKey, "\t", activeHr, "\t", postCount
	printResults(oldKey, activeHrCountDict)
	
        oldKey = thisKey;
	hrValCountDict.clear()

    oldKey = thisKey

    hrValCountDict[thisHr] = 1 + hrValCountDict.get(thisHr, 0)

# calculations for the last key
if oldKey != None:
	activeHrCountDict = findMaxCountForActiveHour()
        #print oldKey, "\t", activeHr, "\t", postCount
	printResults(oldKey, activeHrCountDict)



