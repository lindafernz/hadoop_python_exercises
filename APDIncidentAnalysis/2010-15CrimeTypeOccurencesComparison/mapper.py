#!/usr/bin/python

# Format of each line is:
# Incident Report Number,Crime Type,Date,Time,LOCATION_TYPE,ADDRESS,LONGITUDE,LATITUDE,Location 1\n
# We need to write them out to standard output, separated by a tab

import sys

# simple class inheriting from object class
class NodeData(object):
	staticvarFirstLine = 0

for line in sys.stdin:
    if NodeData.staticvarFirstLine == 0 :
	NodeData.staticvarFirstLine = 1
    else:
	data = line.strip().split(",")
	if len(data) == 9:
		crimeType = data[1]

		date = data[2]
		#data format is :09/29/2015. we just use the year
		year = (date.strip().split("/"))[2]

		addr = data[5]
		
		hasNoLongLat = bool(0)
		if data[6] is not "" and data[7] is not "":
			longitude = data[6].strip()
			latitude = data[7].strip()
		else:
			hasNoLongLat = bool(1)
		
			
		# address format is "12400 BLOCK N MOPAC EXPY NB" or "1000 BLOCK E YAGER LN" or 
		# with longiture/lat - "E WILLIAM CANNON DR / S IH 35 SVRD SB,-97.77089997,30.19066095"
		if hasNoLongLat:
			addrOutStr = addr
		else:
			#use the long/lat instead of address
			addrOutStr = "{0},{1}".format(longitude,latitude)
		
		print "{0}\t{1}\t{2}".format(addrOutStr, year, crimeType)



