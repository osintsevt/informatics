a,b,c = list(map(int, input().split()))
q=0
if (a==b)and(a==c)and(c==b):
    q+=3
elif (a==b)or(a==c)or(c==b):
    q+=2
print(q)