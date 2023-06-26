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
