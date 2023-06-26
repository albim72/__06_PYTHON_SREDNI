#przykład 1

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
print(biglista)
