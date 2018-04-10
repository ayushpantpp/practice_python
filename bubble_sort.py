import sys
A = [22,33,2,34,4,33,56,44]
for i in range(len(A)):
	for j in range(0,len(A)-i-1):
		if A[j] < A[j+1]:
			A[j] , A[j+1] = A[j+1] , A[j]

	
for k in range(len(A)):
	print A[k]
