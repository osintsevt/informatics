x,y = list(map(float, input().split()))
s = ''
if y<1:
	s+='1'
else:
	s+='0'

if y<-x:
	s+='1'
else:
	s+='0'

if (x**2 + y**2)**0.5<1:
	s+='1'
else:
	s+='0'

if ((x-1)**2 + y**2)**0.5<1:
	s+='1'
else:
	s+='0'


print(s)