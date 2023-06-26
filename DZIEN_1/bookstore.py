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


bk1 = Book(45,"Wiedźmin","Andrzej Sapkowski",41)
print(bk1)
