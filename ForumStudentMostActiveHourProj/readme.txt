
Feature: get the most active hour of the day for each forum student

Input data file: forum_data.tar.gz containing forum_data.tsv
Check forum_node100.txt for small sample of input
Result: Students and Posting Time, Total Number of posts at the positing hour
Basically output for each student what is the hour during which the student has posted the most posts.
If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, print the student-hour pairs on separate lines. The order in which these lines appear does not matter.

For example:
100000003 	05 	13
100000005 	01 	1
100000007 	03 	10
100000008 	20 	6
100000008 	16 	6

assumptions:
1. Ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.
