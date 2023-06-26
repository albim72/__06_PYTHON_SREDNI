import math

#przykład nr 1

def g(x):
    return x*math.sqrt(x)

n=100
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c + n + g(b)
    return n

print(policz(4,7,2,78))
print(policz(y=8,b=6,a=5,c=1))
print(n)

#przykład nr 2

def gh(x,l,k=4,n=3.3333):
    return l+x**3/math.sqrt(k-1)*n

print(gh(2,1,2,1))
print(gh(2,1,2))
print(gh(2,1))
print(gh(4,1,n=5))


#przykład 3
def ranking(*lang,nrrank,**noweargs):
    print(f'ranking języków programowania nr {nrrank}-> pierwsze miejsce: {lang[0]}, '
          f'drugie miejsce: {lang[1]}, trzecie miejsce: {lang[2]}')

ranking("Python","Java","C#",nrrank=23)
ranking("Python","Java","Ruby","C#","JavaScript",nrrank=27)
