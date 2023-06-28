liczby = [56,78,99,67,88,93,92,63,65,67,51,89,97,68,77,75,74,71,90,80]

def get_srednia_ochyl(num):
    average = sum(num)/len(num)
    skalowanie = [x/average for x in num]
    skalowanie.sort(reverse=True)
    return skalowanie

longest,*middle,shortest = get_srednia_ochyl(liczby)

print(f'największa wartość: {longest:0.0%}')
print(f'najmniejsza wartość: {shortest:0.0%}')
