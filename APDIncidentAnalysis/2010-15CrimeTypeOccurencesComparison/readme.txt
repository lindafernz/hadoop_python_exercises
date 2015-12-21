
Feature: get the comparison of the crime type and number of occurrences of the crime for each location in the years 2015 and 2010.

Input data file: APD_Incident_Extract_YTD.csv and APD_Incident_Extract_2010.csv
Check APD_Incident_Extract_YTD_200Records.txt for small sample of input

Result: 
A comparison report has been generated to analyse the occurences of crime types in Austin county in the years 2015 and 2010.
Address has been uses in its raw format -see assumptions below.

output format is: ADDRESS	CRIME_TYPE	<YEAR1>	CRIME_COUNT	<YEAR2>	CRIME_COUNT...

Example output records:

-97.62918938,30.28115242	ABANDONED VEH	2015	1	2010	2	
-97.62918938,30.28115242	CRASH/LEAVING THE SCENE	2015	12	2010	10	
-97.62918938,30.28115242	THEFT	2015	2	2010	4	
-97.62918938,30.28115242	PUBLIC INTOXICATION	2015	2	2010	3	
-97.62918938,30.28115242	FAMILY DISTURBANCE	2015	3	2010	1
...
US HWY 290 / N IH 35	FALSE BURGLAR ALARM	2015	53	2009	1	2010	308	
US HWY 290 / N IH 35	DWI	2015	3443	2014	1	2009	1	2010	4659	
US HWY 290 / N IH 35	FRAUD DESTRUCTION OF A WRITING	2015	11	2009	1	2010	7	
US HWY 290 / N IH 35	BURGLARY OF COIN-OP MACHINE	2015	86	2010	110	
US HWY 290 / N IH 35	MONEY LAUNDERING	2015	8	2010	1	
US HWY 290 / N IH 35	DWI 2ND	2015	635	2010	539	
US HWY 290 / N IH 35	VOCO SOLICITATION PROHIBIT	2015	188	2010	988	
US HWY 290 / N IH 35	ASSAULT BY CONTACT FAM/DATING	2015	963	2014	4	2009	1	2010	436	
...
ZILKER PARK	CRED CARD ABUSE - OTHER	2015	771	2014	30	2009	50	2010	827	
ZILKER PARK	VIOL CITY ORDINANCE - OTHER	2015	654	2014	1	2010	1231	
ZILKER PARK	ACCIDENTAL DROWNING DEATH	2015	6	2010	4	

Assumptions:
1. No apartment numbers/suite/building numbers/zipcode information is available in the public datasets. So the input has been analyzed with the available information of the address or latitude/longitude in the dataset.
2. Many of the results show records for 2008, 2009, 2011, 2012 etc. The public dataset names indicate that the records will be from 2010 and YTD(2015), but it is apparent that it also contains records from other years. This is what the raw public dataset originally has and it has been analyzed without any modification or elimiations.

