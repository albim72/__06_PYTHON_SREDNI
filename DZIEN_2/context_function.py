from contextlib import contextmanager

@contextmanager
def context_string(string_input):
    print('Otworzenie managera...\n')

    swapped = string_input.swapcase()
    try:
        yield swapped
    except ValueError as e:
        print('błąd poboru danych...')
    finally:
        print("\nZamknięcie działania...\n")

    print("\n koniec działania kontekst managera!!!\n")

with context_string('wielkie i ważne wydarzenie dnia: wschód SŁOŃCA...') as sws:
    print(sws)
