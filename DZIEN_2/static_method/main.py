from oblicz import Obliczenia
from daty import Dates


print(f"wartość wynosi: {Obliczenia.moblicz(2,7,4)}")

obl = Obliczenia(1,4,6)
print(obl.moblicz(4,8,9))


date = Dates("13-12-2015")
dateFromDB = "13/12/2018"
dateWithDash = Dates.toDashDate(dateFromDB)
d1 = date.getDate()
d2 = dateWithDash
if(d1 == d2):
    print("Identyczne daty")
    print(d1," - ", d2)
else:
    print("różne daty!")
    print(d1," - ",  d2)
