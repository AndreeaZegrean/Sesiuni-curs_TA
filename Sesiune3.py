# Operatori aritmetici
import math

suma = 0
suma = suma + 2
print(suma)

suma = suma - 1
print(suma)

suma = suma * 2
print(suma)

suma = suma / 5
print(suma)

suma = suma // 5  # flor division
print(suma)
print(3 // 2)  # ia partea intreaga
print(3.1 // 2.3)  # nr de tip float ne arata partea intreaga + zecimala

print(2 ** 3)  # exponent - 2 la puterea 3

print(math.sqrt(144))  # radical
print(int(math.sqrt(144)))  # radical - transforma nr de tip float in int

# aflarea restului impartirii prin %
print(7 % 2)  # rez = 0

# Operatori de atribuire
suma = 2
suma = suma * 3
suma *= 3  # inmultire
print(suma)

suma /= 3  # impartire
print(suma)

# Operatori de comparare, va afisa true sau false

print(2 == 3)
print(2 != 3)
print(2 <= 4)
print(2 < 4)
print(suma > 3)

# Operatori logici ( AND, OR, NOT )

# si logic = and - va returna true daca ambele conditii returneaza true
print(suma > 3 and suma != 5)

# daca una din conditii nu este indeplinita va returna false
print(suma > 3 and suma != 5 and suma != 6)

# daca una din conditii este true, va returna true rezultatul final
# prioritare are and, apoi or
print(suma > 3 and suma != 5 or suma != 6)  # = true
print(suma < 3 and (suma != 5 or suma == 6))  # false

# se evalueaza mai intai NOT, apoi AND, apoi OR
# not = negatia unei conditii
print(not suma < 3 and suma != 5 or suma == 6)  # true
print(not 1 == 2 or 1 + 1 == 2 and 1 + 2 == 6)  # true
# print(True or 1 + 1 == 2 and 1 + 2 == 6)
# print(True or False - ultima operatei) = true / OR-ul nu conteaza

# ASSERT - verifica egalitatea dintre un rezultat asteptat si un rezultat afisat
# returneaza True sau False
assert suma == 6
assert suma > 3

# daca conditia este falsa, se opreste executia si ne afiseaza eroare
# assert suma > 12

# IF, ELIF, ELSE
# IF intervine in momentul in care

numar = -2
if numar > 0:
    print('numarul este pozitiv')
else:
    print('numarul este negativ')
print('------------------')

if numar > 0:
    print('numarul este pozitiv')
print('executia s-a incheiat')
print('-----------------')

if numar < 0:
    print('numarul este negativ')
    print('executia s-a incheiat')
print('-------------------')

if numar > 0:
    print('numarul este pozitiv')
elif numar == 0:
    print('numarul este egal cu 0')
elif numar < 0:
    print('numarul este negativ')
else:
    print('executia s-a finalizat')
print('-----------------')

numar = 1
if numar > 1:
    print('numarul este pozitiv')
elif numar == 0:
    print('numarul este egal cu 0')
elif numar < 0:
    print('numarul este negativ')
else:
    print('executia s-a finalizat')
