#!/usr/bin/python

import sys

oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the authorId, val is the added_at time's hour value
#

# class to define for each year's APD record of crimetype
class ApdRecord(object):
	"""class to define for each year's APD record of crimetype
	"""

	def __init__(self, crimeType):
		self._crimeType = crimeType
		# dict for storing the year, count of incidences of this crimetype
		self._yrCountDict = {}

	@property
	def yrCountDict(self):
		return self._yrCountDict

	@property
	def crimeType(self):
		return self._crimeType

	"""method for adding to the year's record of crimetype
	"""
	def addYearRecord(self, yrVal):
		self._yrCountDict[yrVal] = 1 + self._yrCountDict.get(yrVal, 0)


#dict for classes as per the year of the incident
crimeTypeApdClassDict = {}

def printResults(addr):
	outStr = ""
	for cType, apdObj in crimeTypeApdClassDict.iteritems():
		if len(apdObj.yrCountDict) > 1:
			outStr = "{0}\t{1}\t".format(addr, cType)
			for yrVal, crimeCount in apdObj.yrCountDict.iteritems():
				outStr += "{0}\t{1}\t".format(yrVal, crimeCount)
				#print addr, "\t", cType, "\t", yrVal, "\t", crimeCount
			print outStr
			outStr = ""


# simple class inheriting from object class
class NodeData(object):
	staticvarFirstLine = 0

for line in sys.stdin:
    if NodeData.staticvarFirstLine == 0 :
	NodeData.staticvarFirstLine = 1
	# print the first line showing format of output
	print "ADDRESS\tCRIME_TYPE\t<YEAR1>\tCRIME_COUNT\t<YEAR2>\tCRIME_COUNT..."

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisYr, thisCrimeType = data_mapped

    # done processing all values of thisKey, so make the decisions and reset variables to move onto to next key
    if oldKey and oldKey != thisKey:
	printResults(oldKey)	
        oldKey = thisKey;

    oldKey = thisKey

    # look for the class object which holds all info for this crime type
    apdObj = crimeTypeApdClassDict.get(thisCrimeType)
    if not apdObj:
	apdObj = ApdRecord(thisCrimeType)
	crimeTypeApdClassDict[thisCrimeType] = apdObj

    apdObj.addYearRecord(thisYr)

# calculations for the last key
if oldKey != None:
	printResults(oldKey)



