import sys

arg1 = int(input())
arg2 = int(input())
arg3 = []
filled = 0
for i in range(arg2):
    arg3.append(int(input()))

bottles=sorted(arg3)

while arg1 >= bottles[0]:
    if bottles[0] < arg1:
        filled += 1
        val = bottles[0]
        bottles.remove(val)
        arg1 -= val

print filled
