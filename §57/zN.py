x,y = list(map(float, input().split()))
if (x**2+y**2<0)and((y>x)or((x<0)and(y<0))):
    print('YES')
else:
    print('NO')