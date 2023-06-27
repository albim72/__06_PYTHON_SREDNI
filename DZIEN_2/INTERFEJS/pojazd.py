from ipojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie(self, odl, litry):
        return litry*100/odl

    def kosztyprzejazdu(self, odl, litry, cena_l):
        return self.spalanie(odl,litry)*(odl/100)*cena_l
