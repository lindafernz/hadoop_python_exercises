#!/usr/bin/python

import sys


# Loop around the data
# It will be in the format key\tval
# Where key is the location, val is driving-related incident type
#
# All the incident types will be listed for a locaton
# then the key will change and we'll be dealing with the next record


class BaseAddressType(object):
	
	def formattedAddress(self):
		pass	
		

class BlockRangeAddress(BaseAddressType):

	def __init__(self):
		self._highBlk = int(0)
		self._lowBlk = int(99999)
	
	def formattedAddress(self):
		if self._lowBlk == int(99999)  and self._highBlk == 0 :
			retStr = ""
		elif self._lowBlk == self._highBlk :
			retStr = "{0}".format(self._lowBlk)
		else :
			retStr = "{0}-{1}".format(self._lowBlk, self._highBlk)	

		return retStr

	"""method for adding block to the range
	"""
	def addBlock(self, block):
		self._highBlk = max(self._highBlk , int(block))
		self._lowBlk = min(self._lowBlk , int(block))
		#if self._highBlk < int(block):
		#	self._highBlk = int(block)
		#
		#if self._lowBlk > int(block):
		#	self._lowBlk = int(block)


class CoordinatesAddress(BaseAddressType):
	
	def __init__(self, longi, lati):
		self._longitude = longi
		self._latitude = lati

	def formattedAddress(self):
		return "{0},{1}".format(self._longitude, self._latitude)	


# class to store information about the incident's location & crime type/occurences dict
class LocIncidentDetails(object):
	"""class to store information about the incident's location & crime type/occurences dict
	"""

	def __init__(self, addrType):
		# this addr is of BaseAddressType type
		self._addrType = addrType
		# dict for storing the crime type, count of occurences of this crimetype
		self._incTypeCountDict = {}

	@property
	def incTypeCountDict(self):
		return self._incTypeCountDict

	@property
	def addrType(self):
		return self._addrType

	"""method for adding to the year's record of crimetype
	"""
	def addCrimeOccurence(self, cType):
		self._incTypeCountDict[cType] = 1 + self._incTypeCountDict.get(cType, 0)


#simple list of values
class AddressTypes:
	BLOCK_RANGE = 1;
	COORDINATES = 2;

#
class AllIncidentDetails(object):

	def __init__(self):
		self._incDetailsDict = {}

	@property
	def incDetailsDict(self):
		return self._incDetailsDict

	"""method for adding incident details to the list
	"""
	def addIncident(self, addrRem, crimeType):

		if addrRem is not "":
			addrRemSplit = addrRem.split(",")
		else :
			addrRemSplit = ""

		# longitude, lati type 
		if len(addrRemSplit) == 2:
			#check if the coordinate type address was added before
			if AddressTypes.COORDINATES in self._incDetailsDict:
				incDet = self._incDetailsDict.get(AddressTypes.COORDINATES)
				incDet.addCrimeOccurence(crimeType)
			else :
				incDet = LocIncidentDetails(CoordinatesAddress(addrRemSplit[0], addrRemSplit[1]))
				incDet.addCrimeOccurence(crimeType)

				self._incDetailsDict[AddressTypes.COORDINATES] = incDet
				
		else:
			try:
				blockNum = int(0)
				if addrRem is not "":
					blockNum = int(addrRem)
			except ValueError:
				pass
				
			if AddressTypes.BLOCK_RANGE in self._incDetailsDict:
				#get the block range type address instance
				incDet = self._incDetailsDict.get(AddressTypes.BLOCK_RANGE)
				incDet.addrType.addBlock(blockNum)
				incDet.addCrimeOccurence(crimeType)
			else :
				# if it was not existing, create one by default
				blkRangeAddr = BlockRangeAddress()
				blkRangeAddr.addBlock(blockNum)
				
				incDet = LocIncidentDetails(blkRangeAddr)
				incDet.addCrimeOccurence(crimeType)

				self._incDetailsDict[AddressTypes.BLOCK_RANGE] = incDet
				
	

#method for printing incident details 
def printResults(locKey, allIncs):
	
	for addrTypeVal, incDetails in allIncs.incDetailsDict.iteritems():
		addrPartStr = incDetails.addrType.formattedAddress()
		for incType, incCount in incDetails.incTypeCountDict.iteritems():
			if addrTypeVal == AddressTypes.BLOCK_RANGE:
			        print addrPartStr, "\t", locKey, "\t", incType, "\t", incCount
			elif addrTypeVal == AddressTypes.COORDINATES:
			        print locKey, "\t", addrPartStr, "\t", incType, "\t", incCount

# structure for holding all details of all incidents in 1 location, initialized by default for 1st record
allIncDetails = AllIncidentDetails()
oldKey = None

######## Reducer code ########
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisAddrPart2, thisIncident = data_mapped

    if oldKey and oldKey != thisKey:
        printResults(oldKey, allIncDetails)
        oldKey = thisKey;
	if allIncDetails is not None:
		del allIncDetails
		allIncDetails = AllIncidentDetails()

    oldKey = thisKey
    allIncDetails.addIncident(thisAddrPart2.strip(), thisIncident.strip())

if oldKey != None:
	printResults(oldKey, allIncDetails)

