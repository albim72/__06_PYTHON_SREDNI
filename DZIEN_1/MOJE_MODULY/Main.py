# import dane
# import dane as dn
from dane import nrfilii as filia
from dane import book as bk
from funkcje.bfunckje import czytaj_liste,czytaj_slownik


print("____________ dane ______________")
print(filia)
print(bk)

print("____________ dane przez funkcje ______________")
print(czytaj_liste(filia))
print("_____________________")
print(czytaj_slownik(bk))
