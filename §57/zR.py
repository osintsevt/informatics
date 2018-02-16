x,y = list(map(float, input().split()))
if (x**2+y**2<1)or((0<x<1)and(0<y<1)):
    print('YES')
else:
    print('NO')