#przykład 1
import math


def witaj(imie):
    return f'dziękujemy za założenie konta: {imie}'

def egzamin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, zaliczenie: {zaliczono}'

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(egzamin,"Olga",57,True))


#przykład 2

def rejestracja(oplata):
    def lista_zawodnikow():
        return "jesteś na liście zawodników - opłata wniesiona!"

    def brak():
        return "brak wpłaty - za 3 dni zostaniesz usunięy z listy!"

    def error():
        return "błąd w kodzie opłaty: 1- opłacono, 2 - nieopłacono, 3 - błędny kod!"

    if oplata == 1:
        return lista_zawodnikow
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(9)())

#przykład 3

biglista = [2*i+1 for i in range(100_000) if i%2!=0]
# print(biglista)

#przykład 4

def startstop(funkcja):
    def wrapper(*args):
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka!")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodzinowym torcie!")

@startstop
def f(x):
    print(2*x)

dmuchanie("świeczek")

f(34)

def policz(funkcja):
    def wrapper(*args):
        print("pdostawienie funkcji f(x)... i spierwiastkowanie jej wyniku")
        print(f"wynik: {math.sqrt(funkcja(*args))}")
    return wrapper


@policz
def suma(a,b):
    return a+b

@policz
def podiloczyn(x,y):
    return 2*x*y

suma(5,5)
podiloczyn(5,5)
