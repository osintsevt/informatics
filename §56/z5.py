x1,y1 = list(map(float, input().split()))
x2,y2 = list(map(float, input().split()))
x = x2-x1
y = y2-y1
z = (x**2+y**2)**0.5
print('{0:.3f}'.format(z))