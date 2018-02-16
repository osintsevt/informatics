from random import seed, randint
seed()
m,n = list(map(int, input().split()))
print('{a} {b} {c} {d} {e}'.format(a = randint(m,n),b = randint(m,n),c = randint(m,n),d = randint(m,n),e = randint(m,n),))