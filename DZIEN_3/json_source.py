import json

jsource = '{"imie":"Jan","nazwisko":"Nowak","wiek":40,"miasto":"Zamość"}'
print(jsource)
print(type(jsource))

osoba = json.loads(jsource)
print(osoba)
print(type(osoba))
print(osoba["nazwisko"])
