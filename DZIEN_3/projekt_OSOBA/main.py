class Osoba:
    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self._wiek = wiek
        self._waga = waga
        self._wzrost = wzrost
    
    @property
    def wiek(self):
        return self._wiek
    
    @wiek.setter
    def wiek(self,lata):
        self._wiek = lata

    @property
    def waga(self):
        return self._waga

    @waga.setter
    def waga(self, kg):
        self._waga = kg

    @property
    def wzrost(self):
        return self._wzrost

    @wzrost.setter
    def wiek(self, cm):
        self._wzrost = cm
    
    
