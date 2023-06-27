class Obliczenia:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def moblicz(x,y,z):
        return (x+y)*z

Obliczenia.moblicz = staticmethod(Obliczenia.moblicz)

print(f"wartość wynosi: {Obliczenia.moblicz(2,7,4)}")

obl = Obliczenia(1,4,6)
print(obl.moblicz(4,8,9))
