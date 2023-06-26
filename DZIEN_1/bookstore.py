class Book:
    #deklaracja stanu
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #opis zachowania
    def create_book(self):
        print("utworzenie nowe książki")

    def print_book(self):
        print(f"książka: {self.tytul}, autor: {self.autor}, cena: {self.cena}, oprawa: {self.oprawa}")

    def rabat(self,procent):
        return self.cena*(procent/100)

    def getoprawa(self):
        return self.oprawa

    def getcena(self):
        return self.cena

    def setoprawa(self,nopr):
        self.oprawa = nopr

    def setcena(self,ncena):
        self.cena = ncena


bk1 = Book(45,"Wiedźmin","Andrzej Sapkowski",41)
print(bk1)
# bk1.oprawa = "twarda"
# bk1.cena = 78
bk1.setoprawa("twarda")
bk1.setcena(66)
print(f'nowa cena: {bk1.getcena()} zł')
bk1.print_book()
print(f'rabat: {bk1.rabat(11)} zł')
print(f'kwota do zapłaty {bk1.cena - bk1.rabat(11)} zł')

print("_"*30)
bk2 = Book(89,"Hobbit","J.R.R. Tolkien",40)
# bk1.setoprawa("twarda")
# bk1.setcena(66)
print(f'nowa cena: {bk2.getcena()} zł')
bk2.print_book()
print(f'rabat: {bk2.rabat(11)} zł')
print(f'kwota do zapłaty {bk2.cena - bk2.rabat(11)} zł')
