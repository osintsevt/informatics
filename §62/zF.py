x,n = list(map(int, input().split()))
s = ''
for i in list(reversed(range(x,x+n))):
    s+=str(i)+' '
print(s)