# FUNCTIILE reprezinta blocuri de cod reutilizabile care
# sunt definite cu scopul de a limita nr de linii de cod pt a scrie
# si a face programul sa fie mai modular si respectiv mai usor de
# citit si de gestionat

'''O functie are urmatoarele componente:

Inceputul functiei: def
Numele functiei -> free text (se recomanda formatul snake_case)
Inceputul corpului functiei -> marcat de caracterul “:”
Corpul functiei -> marcat de spatiu de la marginea fisierului (indentare). Atunci cand se iese din indentare se iese din corpul functiei
Parametri -> optionali
Instructiune return -> optionala
'''

def my_function():
    print('Hello from my_function')
my_function()

def my_function():
    return 3
print(my_function())

# x este un parametru obligatoriu
def my_function(x):
    return 5*x
print(my_function(2))

# introducere data de la tastatura cu input
# y = int(input('Numarul este:'))
# print(my_function(y))

# parametri obligatorii
def suma_2_numere(x, y):
    return x + y
print(suma_2_numere(3, 4))

# parametri nu sunt necesari pt ca se face in interiorul functiei
def calculator():
    operatie = input('Introduceti operatia dorita din +,-,/,* ')
    primul_numar = int(input('Introduceti primul nr'))
    al_doliea_numar = int(input('Introduceti al 2-lea nr'))
    if operatie == '+':
        return primul_numar + al_doliea_numar
    elif operatie == '-':
        return primul_numar - al_doliea_numar
    elif operatie == '*':
        return primul_numar * al_doliea_numar
    elif operatie == '/':
        return primul_numar / al_doliea_numar
# print(calculator())

# ex cu parametru implicit ( x = 1, y =2 )
print(suma_2_numere(4, 7))
def suma_2_numere(x = 1, y =2):
    return  x + y
print(suma_2_numere())

# ARGS - un numar indefinit de parametri
# = o lista
def suma_numere(*args):
    suma = 0
    for x in args:
        suma = suma + x
    return suma
print(suma_numere()) # nici un argument pt ca nu avem valori
print(suma_numere(1, 2, 3))
print(suma_numere(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# nr max dintr-o lista args
def max_numere(*args):
    max = 0
    for y in args:
        if max < y:
            max = y
    return max
print(max_numere(4, 8, 35))

# parcurge din dictionar - numar1 + 2 sunt chei valori
def suma_numere(**kwargs):
    suma = 0
    for x in kwargs.values():
        suma = suma + int(x)
    return suma
print(suma_numere(numar1 = 2, numar2 = 5))
print(suma_numere(**{'numar1':4, 'numar2':6}))

# Tratarea exceptiilor
try:
    print(10/0)
except:
    print('Impartirea la zero nu este permisa')

try:
    my_list = [1, 2, 3]
    print(my_list[1])
except:
    print('Elementul nu exista')

x = -1
if x < 0:
    raise Exception('Nu se permit numere negative')

