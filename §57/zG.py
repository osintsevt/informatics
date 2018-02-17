n = int(input())
a = 0
if n in [1,3,5,7,8,10,12]:
	a = 31
elif n in [4,6,9,11]:
	a = 30
elif n==2:
	a = 28
print(a)