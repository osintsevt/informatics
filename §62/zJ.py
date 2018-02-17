from random import randint
a,b,n = list(map(int, input().split()))
s = ''
A = []
v = 0
for i in range(n):
    A.append(str(randint(a,b)))
    
for i in range(len(A)):
    s+=A[i]+' '
print(s)

for i in range(len(A)):
    if ((((int(A[i]))//10)%10)%2==0)and(int(A[i])>9):
        v+=1
print(v)
