n = int(input())
s = 'NO'
if 3<=n<=5:
	s = 'spring'
elif 6<=n<=8:
	s = 'summer'
elif 9<=n<=11:
	s = 'autumn'
elif (n==12)or(1<=n<=2):
	s = 'winter'
print(s)