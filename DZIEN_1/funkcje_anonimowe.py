print((lambda e:e+2)(12))

b = lambda u,w: 2*u/w

print(b(2,7))

h = lambda a,b,c=5.5:(a+b)/c

print(h(5,12,4))
print(h(5,12))

def multi(n):
    return lambda a:a*n

print(multi(8)(6))
