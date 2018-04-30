import sys
def nextString ():
	string = raw_input()
	digit = list(string)
	for i in range(len(digit)-1,-1,-1):
		if digit[i] == 'Z':
			digit[i] = 'A'
			if i == 0:
				digit.append('A')
		else:
			digit[i] = chr(ord(digit[i]) + 1)
			break
	return ''.join(digit)
	



print(nextString())

		
