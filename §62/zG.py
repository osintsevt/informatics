x,d,n = list(map(int, input().split()))
s = ''
for i in list(reversed(range(n))):
    s+= str(x+i*d) +' '
print(s)