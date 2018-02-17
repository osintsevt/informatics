n = int(input())
s = ''
for i in list(reversed(range(1,n+1))):
    s+=str(2**i)+' '
print(s)
    