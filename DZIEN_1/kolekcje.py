print("kolekcje języka Python")
a = 55
print(a)
print(type(a))

a = "zielone"

print(a)
print(type(a))

b:float = 9.567
print(b)
print(type(b))

b = True
print(b)
print(type(b))

imiona = ["Jan","Monika","Leon","Olaf","Halina","Jan","Nadia","Maria","Leon"]

print(imiona)
print(imiona[0])
print(imiona.count("Jan"))
print((imiona[2:6]))

imionaparz = imiona[::2]
print(imionaparz)

mi = imiona[2]
print(mi)

print(mi[::-1])


import copy

team = imiona
t1 = list(imiona)
t2 = imiona[:]
t3 = copy.deepcopy(imiona)

print(type(team))
print(f'lista imiona: {imiona}')
print(f'lista team: {team}')

imiona[2:4] = ["Feliks","Paweł","Roma","Daria"]
print(f'lista imiona po zmianie: {imiona}')
print(f'lista team po zmianie: {team}')
print(f'lista t1 po zmianie: {t1}')
print(f'lista t2 po zmianie: {t2}')
print(f'lista t3 po zmianie: {t3}')

#krotka -> lista niemutowalna -> tuple
miasta = ("Kraków","Lublin","Gdańsk","Wrocław","Kraków","Warszawa")

#zbiór - set

kolory = {"zielony","biały","czerwony","niebieski","brązowy","zielony"}
print(kolory)
print(kolory)
print(kolory)

kolory.remove("zielony")
print(kolory)

kolory.discard("burgundowy")
print(kolory)

kolory.discard("czerwony")
print(kolory)

#słownik
osoba = {
    "imię":"Jan",
    "nazwisko":"Kot",
    "wiek":56,
    "miasto":"Rzeszów",
    "miasto urodzenia":"Rzeszów",
    "nazwisko":"Konot"
}

print(osoba)
print(type(osoba))
print(osoba["imię"])

osoba["miasto"] = "Sanok"
print(osoba)
osoba["zawód"] ="informatyk"
print(osoba)

print(osoba.keys())
print(osoba.values())
print(osoba.items())

print("_______________ klucze _______________")
for x in osoba:
    print(x)

print("_______________ wartości _______________")
for x in osoba:
    print(osoba[x])

print("_______________ wartości [values] _______________")
for x in osoba.values():
    print(x)

print("_______________ items _______________")
for x,y in osoba.items():
    print(f'{x}: {y}')
