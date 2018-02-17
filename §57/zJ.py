x,y = list(map(float, input().split()))
if ((x**2 + y**2)>4)and(y>0)and(x<2)and(y<x):
	print('YES')
else:
	print('NO')