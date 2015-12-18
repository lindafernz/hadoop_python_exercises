#!/usr/bin/python

# Format of each line is:
# "id"\t"title"\t"tagnames"\t"author_id"\t"body"\t"node_type"\t"parent_id"\t"abs_parent_id"\t"added_at"\t"score"
#\t"state_string"\"last_edited_id"\t"last_activity_by_id"\t"last_activity_at"\t"active_revision_id"\t"extra"
#\t"extra_ref_id"\t"extra_count"\t"marked"\n
#
# 
# We need to write them out to standard output, separated by a tab

import sys

class NodeData(object):
	staticvarFirstLine = 0
	@classmethod
	def myclassmethod():
		pass
	
	@staticmethod
	def mystaticmethod():
		pass


for line in sys.stdin:
    if NodeData.staticvarFirstLine == 0 :
	NodeData.staticvarFirstLine = 1
    else:
	data = line.strip().split("\t")
	if len(data) == 19:
		authId = data[3]
		entryDateTime = data[8]

		#note that each arg has a double quote around the actual value
		# format of added_at is "2012-02-25 08:09:06.787181+00" or "2012-03-01 02:03:26.803793+00"
		dateTimeSplit = entryDateTime.strip("\"").split(" ")
		if len(dateTimeSplit) == 2:
			date, time = dateTimeSplit
			timeSplit = time.strip().split(":")
			print "{0}\t{1}".format(authId.strip("\""), timeSplit[0])

