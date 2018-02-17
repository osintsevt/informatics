x,y = list(map(float, input().split()))
if (y<1)and(x>0)and((y>x-1)or(x**2+y**2<1)):
    print('YES')
else:
    print('NO')