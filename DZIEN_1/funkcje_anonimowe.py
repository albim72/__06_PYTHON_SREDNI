print((lambda e:e+2)(12))

b = lambda u,w: 2*u/w

print(b(2,7))

h = lambda a,b,c=5.5:(a+b)/c

print(h(5,12,4))
print(h(5,12))

def multi(n):
    return lambda a:a*n

print(multi(8)(6))

liczba = [3,12,5,88,9,14,117,-4,0,-24,13,15,1,999,2]

parz = list(filter(lambda x:x%2==0,liczba))
print(parz)

cube = list(map(lambda x:x**3,liczba))
print(cube)

cubeset = set(map(lambda x:x**3,liczba))
print(cubeset)

def fiveplus(x):
    return x+5

five = list(map(fiveplus,liczba))
print(five)
 
