# print('Buna seara!')
# print('Hello!')
# print('1234')

# O variabila este o adresa de memorie care stocheaza o anumita valoare
# x este de tip string care reprezinta o secventa de caractere/propozitie
x = 'Buna seara!'
print(x)

# a si b sunt de tipul int care sunt numere intregi
a = 3
b = 5
print(a + b)

# a si b sunt de tipul float care sunt numere reale cu zecimale
a = 1.2
b = 10.1
print(a + b)

# se pot printa mai multe valori odata, numele variabilelor sunt case sensitive
myvar = 3
myVar = 7
print(myvar, myVar)

myvar = 'abcd'
print(myvar)

myvar, myVar = 11, 10
print(myvar, myVar)

# tip de data boolean
Sunt_la_curs = True
print(Sunt_la_curs)

Sunt_la_curs = False
print(Sunt_la_curs)

# definire constanta (cu litere mari) definim constante cand nu se schimba valoarea
SUNT_INSCRIS_LA_CURS = True
print(SUNT_INSCRIS_LA_CURS)

DATA_NASTERE = '29.04.1988'
# print('DATA_NASTERE')
print(DATA_NASTERE)

# type este o functie predefinita din pyton care ne ajuta sa expunem tipul de data al unei variabile (ex. int, boolean)
print(type(DATA_NASTERE))
X = type(myvar)
print(X)

print(type(myvar))

# type casting - modificam (fortam) un anumit tip de date pentru variabile ( din string in int - numeric )
a = '2'
print(type(int(a)))
print(type(a))

print(a + '3')  # concatenare/lipie  - alatura numerele - sir de caractere
print(int(a) + 3)  # le aduna

a = ('Avram')
print(a + ' 4 ')
# print(int(a))

c = 10.4  # convertire din boolean in int - ia doar partea intreaga
print(int(c))

# print(3+'Ana')
print(str(3) + ' Ana')

# printare cu formatare - nu se mai face type casting la fiecare variabila, punem intre {} ce valori avem nevoie,
# iar ulterior adaugam si textul daca este necesar
print(f'{3} Ana')

# {} ajuta sa acceseze valoarea variabilei mentionate intre {}
nume = 'Bogdan'
nota = 10
print(f'{nume} are nota {nota}')

# functia input ne ajuta sa preluam date de la tastatura
a = input('Introduceti primul numar: ')
b = input('Introduceti al doilea numar: ')
print(a + b)  # concatenare celor 2 nr
print(int(a) + int(b))  # suma celor 2 nr
print(int(a) - int(b))  # scaderea celor 2 nr

"""
Comentarii
pe mai
multe linii
"""
