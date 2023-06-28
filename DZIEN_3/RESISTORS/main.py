from oldresistor import OldResistor


print("__________________________________________")
r0 = OldResistor(10.22E2)
print(f"_______________ klasa {r0.__class__.__name__} ________________")
print(r0)
print(r0.get_ohms())
r0.set_ohms(3.33E3)
print(r0.get_ohms())
