x,y = list(map(float, input().split()))
if (y>=2*x**2)and(x<=1)and(y>=1-x):
    print('YES')
else:
    print('NO')