n = int(input())
s = ''
m = 1
A = []
for i in range(n):
    A.append(m)
    if i != 0:
        m = A[i] + A[i-1]
for i in range(len(A)):
    s+=str(A[i])+' '
    
print(s)