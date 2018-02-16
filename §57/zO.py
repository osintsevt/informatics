x,y = list(map(float, input().split()))
if (x**2+y**2<1)and not((y<abs(x))and(x<0)):
    print('YES')
else:
    print('NO')