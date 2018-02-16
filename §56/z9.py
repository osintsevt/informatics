from random import seed, uniform
seed()
m,n = list(map(float, input().split()))
print('{a:.3f} {b:.3f} {c:.3f} {d:.3f} {e:.3f}'.format(a = uniform(m,n),b = uniform(m,n),c = uniform(m,n),d = uniform(m,n),e = uniform(m,n),))