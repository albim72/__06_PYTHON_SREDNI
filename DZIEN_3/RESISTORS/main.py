from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance


print("__________________________________________")
r0 = OldResistor(10.22E2)
print(f"_______________ klasa {r0.__class__.__name__} ________________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(3.33E3)
print(r0.get_ohms())

r1 = Resistor(50E3)
print(f"_______________ klasa {r1.__class__.__name__} ________________")

print(r1.ohms)
r1.ohms = 5.5E3
print(r1.ohms)

print(f'układ elektryczny:\n'
      f'oporność: {r1.ohms} om\n'
      f'napięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A\n')

r2 = VoltageResistance(1.2E3)
print(f"_______________ klasa {r2.__class__.__name__} ________________")

print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 48
print(f'napięcie  prądu: {r2.voltage} V')
print(f'natężenie  prądu: {r2.current} A')

r3 = BoundedResistance(1.1E2)
print(f"_______________ klasa {r3.__class__.__name__} ________________")
try:
      print(f'oporność pierwotna układu: {r3.ohms}')
      r3.ohms = 15
      print(f'oporność wtórna układu: {r3.ohms}')
except ValueError as d:
      print(d)

