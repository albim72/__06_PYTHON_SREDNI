import json

jsource = '{"imie":"Jan","nazwisko":"Nowak","wiek":40,"miasto":"Zamość"}'
print(jsource)
print(type(jsource))

osoba = json.loads(jsource)
print(osoba)
print(type(osoba))
print(osoba["nazwisko"])

auto = {
    "marka":"Jeep",
    "model":"Cherokee",
    "rocznik":2020,
    "poj":4.8
}

print(auto)
jsonauto = json.dumps(auto,indent=4)
print(jsonauto)

with open("auto.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

with open("auto.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(type(auto_dict))

print("_________________________________________________")

info = '{"organizacja":"Fundacja BIOTECH","miasto":"Lublin","kraj":"Polska"}'
projekt = {"id":674,"temat":"Innowacyjne technologie AI","kwota":12456000}

z = json.loads(info)
z.update(projekt)
info_new = json.dumps(z, indent=4)
print(info_new)
