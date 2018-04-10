import sys

arr = [22,2,3,2,3,4,5,6]

def check_if_element_exist(arr):
	cnt = 0;
	n = int(input())
	for i in arr:
		if(i == n):
			cnt = cnt + 1;		
	print cnt
	print "Element %s, is repeated %s times!" % (n , cnt)


check_if_element_exist(arr)			

