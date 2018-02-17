a = list(map(int, input('').split(' ')))
A,B,C = a
Max = max(A,B,C)
if (A==B)and(B==C):
    print('0')
elif (A==B)and(B==Max):
    print('A B')
elif (A==C)and(C==Max):
    print('A C')
elif (B==C)and(C==Max):
    print('B C')
elif A==Max:
    print('A')
elif B==Max:
    print('B')
else:
    print('C')