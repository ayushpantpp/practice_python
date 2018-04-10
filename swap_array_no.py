import sys

arr = [22,2,3,2,3,4,5,6]

def swap_array_no(arr, n):
	temp = arr[0]
	for i in range(n):
		arr[i] = arr[i+1]
	arr[n-1] = temp		
	print arr



swap_array_no(arr , 3)			

