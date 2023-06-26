
#przykład nr 1

n=100
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c + n
    return n

print(policz(4,7,2,78))
print(policz(y=8,b=6,a=5,c=1))
print(n)

