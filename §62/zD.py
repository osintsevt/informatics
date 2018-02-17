x,d,n = list(map(int, input().split()))
s = ''
for i in range(n):
    s+= str(x+i*d) +' '
print(s)