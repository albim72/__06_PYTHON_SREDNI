try:
    x = 2
    print(x)
except NameError:
    print("x nie jest zdefiniowany")
except TypeError:
    print("niewłaściwa wartość")
except:
    print("nieoczekiwanhy błąd")
else:
    print(f'podwójny x = {2*x}')
finally:
    y=9
    print(f'ostatnia składowa instrukcji, wypisanie wartości y: {y}')


print("ciąg dalszy programu...")
