from dataclasses import dataclass,astuple,asdict,field

@dataclass
class Person:
    city: str
    firstname:str = "Janek"
    lastname:str = "Kot"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)

    # full_name = firstname + " " + lastname
    def __repr__(self):
        return f"Pracownik: {self.firstname} {self.lastname}, stanowisko: {self.job}"
    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname



os1 = Person("Kraków")
print(os1)
print(os1.full_name)

os2 = Person("Kielce","Olga","Nowak",26,"Prezes")
print(os2)
print(os2.full_name)
print(os2)

print(astuple(os1))
print(asdict(os2))
