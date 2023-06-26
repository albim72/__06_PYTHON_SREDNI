liczby = [56,90,88,100,-45,0,194,888,-1998,2103,188,-34,-100,123,456,901,-564,2,5,6]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    sr_arytm = suma_el/liczba_el
    return minimum,maksimum,rozstep,liczba_el,suma_el,sr_arytm

wynik = pokaz_stat(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,lel,sel,sra = pokaz_stat(liczby)
print(f'wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, liczba elementów: {lel},'
      f'suma wszystkich elementów: {sel}, średnia arytmetyczna: {sra}')
