class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.koloroczu = "brązowe"

    def print_osoba(self):
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm")

    def czypracownik(self):
        return False


os1 = Osoba("Jan",34,101,178)
os1.print_osoba()
print(f'czy osoba jest pracownikiem? {os1.czypracownik()}')


class Firma:
    def __init__(self,nazwa,branza,miasto):
        self.nazwa = nazwa
        self.branza = branza
        self.miasto = miasto

    def show_firma(self):
        print(f"firma {self.nazwa}({self.branza}), miasto:{self.miasto}")



class Pracownik(Osoba, Firma):

    def __init__(self, imie, wiek, waga, wzrost, nazwa,branza,miasto,
                 stanowisko,wynagrodzenie):
        Osoba.__init__(self,imie, wiek, waga, wzrost)
        Firma.__init__(self,nazwa,branza,miasto)
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        print(f'Dane pracownika: {self.stanowisko}, wynagrodzenie: {self.wynagrodzenie} zł')

    def czypracownik(self):
        return True

pr1 = Pracownik("Olga",32,56,167,"ABC","IT","Kraków","Dyrektor",11200)
pr1.print_osoba()
pr1.print_pracownik()
pr1.show_firma()
print(f'czy osoba jest pracownikiem? {pr1.czypracownik()}')


