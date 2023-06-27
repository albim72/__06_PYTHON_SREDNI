def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("nie dziel przez 0!!!")
    except NameError:
        print("zmienne niezdefiniowane...")
    except TypeError:
        print("niewłaściwy typ danych...")
    except Exception as ex:
        print(f"komunikat błędu: {ex}")
    else:
        print(f'wynik = {wynik}')
    finally:
        print("policzmy coś jeszcze!")

try:
    dzielenie(4,5)
    dzielenie(2,0)
    dzielenie(0.1,0.0000034)
    dzielenie(0,0)
    dzielenie(-88,9.999)
    dzielenie(True,3)
    dzielenie("aasfafaf",0)
    #dzielenie(56)
    dzielenie()
except TypeError as f:
    print(f"zbyt mało argumentów -> podaj (x,y): {f}")
