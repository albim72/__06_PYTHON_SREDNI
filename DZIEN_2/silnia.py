import sys

#funkcja silnia n!=1*2*3*...*n dla n>=0
#double -> max: 1.8E+308, min 2.4E-324
#n??? n=171

def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych!")
    wynik = 0
    for i in range(1,n+1):
        wynik *= i
    return wynik
