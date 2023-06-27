import csv
with open("firma.csv",encoding='utf-8') as pc:
    csv_reader = csv.reader(pc,delimiter=";")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'NAZWA KOLUMNY: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} pracuje na stanowisku {row[1]} i ma urodziny w miesiącu: {row[2]}, otrzymuje '
                  f'nagordę finansową w wysokości {row[3]} zł')
            line_count += 1
    print(f'dodano {line_count} linii')
    print(f'dodano {line_count-1} osób')


with open('emp_file.csv','w',encoding='utf-8') as ef:
    emp_writer  = csv.writer(ef,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)

    emp_writer.writerow(('Karol Krot','Finanse','Luty'))
    emp_writer.writerow(['Nadia Król','IT','Luty'])
    emp_writer.writerow(['Olga Nowak','Finanse','Luty'])
