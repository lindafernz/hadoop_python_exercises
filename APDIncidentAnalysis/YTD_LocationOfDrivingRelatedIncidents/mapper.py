#!/usr/bin/python

# Format of each line is:
# Incident Report Number,Crime Type,Date,Time,LOCATION_TYPE,ADDRESS,LONGITUDE,LATITUDE,Location 1\n
# We need to write them out to standard output, separated by a tab

import sys

# simple class inheriting from object class
class NodeData(object):
	staticvarFirstLine = 0

# function to filter the crime types - 
# valid string contains one of the values in {"CRASH", "DWI", "RECKLESS DRIVING", "DRIVING WHILE INTOX"}
def isDrivingRelatedIncident(incStr):
	isMatchFilter = bool(0)
	
	if 'CRASH' in incStr or 'DWI' in incStr or 'RECKLESS DRIVING' in incStr or 'DRIVING WHILE INTOX' in incStr:
		isMatchFilter = bool(1)

	return isMatchFilter


for line in sys.stdin:
    if NodeData.staticvarFirstLine == 0 :
	NodeData.staticvarFirstLine = 1
    else:
	data = line.strip().split(",")
	if len(data) == 9:

		date = data[2]
		#data format is :09/29/2015. we just use the year
		year = (date.strip().split("/"))[2]

		crimeType = data[1]

		# output this indicent if the incident report year is current and it is driving related
		if year == "2015" and isDrivingRelatedIncident(crimeType) :			
			
			addr = data[5].strip();
		
			hasNoLongLat = bool(0)
			if data[6] is not "" and data[7] is not "":
				longitude = data[6].strip()
				latitude = data[7].strip()
			else:
				hasNoLongLat = bool(1)
					
		
			addrPart2 = ""
			# address format is "12400 BLOCK N MOPAC EXPY NB" or "1000 BLOCK E YAGER LN" or "W YAGER LN"
			# with longiture/lat - "E WILLIAM CANNON DR / S IH 35 SVRD SB,-97.77089997,30.19066095"
			if hasNoLongLat:
				addrSplit = addr.strip().split(" ", 2)
				if len(addrSplit) > 2 and addrSplit[1] == 'BLOCK':
					addrPart2 = addrSplit[0] 
					addrOutStr = addrSplit[2]
				else :
					addrPart2 = ""
					addrOutStr = addr
			else:
				#use the long/lat instead of address
				addrPart2 = "{0},{1}".format(longitude,latitude)
				addrOutStr = addr
		
			print "{0}\t{1}\t{2}".format(addrOutStr, addrPart2, crimeType)



