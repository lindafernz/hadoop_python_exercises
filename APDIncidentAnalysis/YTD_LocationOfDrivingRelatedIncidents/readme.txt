
Feature: Get the driving-related incidents reported in the YTD 2015 in the Austin county and the incident locations. Report the location and number of occurences along with the incident type . 

Input data file: APD_Incident_Extract_YTD.csv
Check APD_Incident_Extract_YTD_200Records.txt for small sample of input
The input data has been filtered for the following keywords/phrases to account for the possible driving incidents and related types:
{ "Crash", "DWI", "Reckless Driving", "Driving while intox"}

Result: 
Reports the address of the driving related incident, the exact incident that occured and number of occurences during the current year(2015)
The address is formatted to get more meaningful information as follows. If the address contains a block number, then report the block number range which is basically the lowest-highest value for that address. If no block number exists, just report the complete address. If the longitude, latitude values exists in the input, then report these values as in the input.

This info can be useful for:
- further analysis of the areas or streets or highways where driving incidents rate is high. For example, some areas indicate high occurence of DWIs which may point to bars/restaurants in the area. Those venues can be alerted to be post warnings about drink and drive or be more vigilant of customers consuming high amounts of alcohol, and so on. Another example is areas where crashes are frequent. Those areas may be reviewed for traffic/road/highway code compliance or missing road signs.

output format is: BLOCK_NUMBER_RANGE<if any>	ADDRESS/STREET	LONGITUDE,LATITUDE<if any>	DRIVING_INCIDENT_TYPE	CRIME_COUNT

Example output records:
8400-11900 	ANDERSON MILL RD 	CRASH/NO INJURY 	2
8400-11900 	ANDERSON MILL RD 	DWI  .15 BAC OR ABOVE 	1
8400-11900 	ANDERSON MILL RD 	CRASH/LEAVING THE SCENE 	14
8400-11900 	ANDERSON MILL RD 	CRASH/FAIL STOP AND RENDER AID 	1
8400-11900 	ANDERSON MILL RD 	CRASH/EMS 	1
8400-11900 	ANDERSON MILL RD 	CRASH/CITY VEHICLE 	2
8400-11900 	ANDERSON MILL RD 	CRASH/INTOXICATION ASSAULT 	1
8400-11900 	ANDERSON MILL RD 	CRASH/SERIOUS BODILY INJURY 	2
8400-11900 	ANDERSON MILL RD 	DWI 	11
8400-11900 	ANDERSON MILL RD 	DWI - DRUG RECOGNITION EXPERT 	1
8400-11900 	ANDERSON MILL RD 	DWI 2ND 	1
ANDERSON MILL RD / BROADMEADE AVE 	-97.77639777,30.45319298 	CRASH/LEAVING THE SCENE 	1
ANDERSON MILL RD / N FM 620 RD 	-97.82580522,30.45544917 	DWI 	3
ANDERSON MILL RD / N FM 620 RD 	-97.82580522,30.45544917 	CRASH/LEAVING THE SCENE 	2
ANDERSON MILL RD / N US 183 HWY SVRD NB 	-97.79003189,30.44889001 	DWI 	1
ANDERSON MILL RD / N US 183 HWY SVRD SB 	-97.79094937,30.4486469 	DWI  .15 BAC OR ABOVE 	1
ANDERSON MILL RD / N US 183 HWY SVRD SB 	-97.79094937,30.4486469 	DWI 	1
ANDERSON MILL RD / N US 183 HWY SVRD SB 	-97.79094937,30.4486469 	CRASH/LEAVING THE SCENE 	3
...
WOODROW AVE / W ANDERSON LN 	-97.72323611,30.35251041 	DWI  .15 BAC OR ABOVE 	1
WOODROW AVE / W NORTH LOOP BLVD 	-97.73585962,30.32418231 	CRASH/LEAVING THE SCENE 	1
9700 	WOODSHIRE DR 	DRIVING WHILE INTOX / FELONY 	1
8500 	WOODSTONE DR 	CRASH/LEAVING THE SCENE 	1
100-2100 	WOODWARD ST 	CRASH/CITY VEHICLE 	1
100-2100 	WOODWARD ST 	CRASH/LEAVING THE SCENE 	10
100-2100 	WOODWARD ST 	DWI  .15 BAC OR ABOVE 	4
100-2100 	WOODWARD ST 	CRASH/FAIL STOP AND RENDER AID 	2
100-2100 	WOODWARD ST 	DWI 2ND 	1
100-2100 	WOODWARD ST 	DWI 	5

Assumptions:
1. No apartment numbers/suite/building numbers/zipcode information is available in the public datasets. So the input has been analyzed with the available information of the address or latitude/longitude in the dataset.
2. The filtering/input data modification for the keywords related to driving incidents can be adjusted/reviewed if, for example, new types are added.
