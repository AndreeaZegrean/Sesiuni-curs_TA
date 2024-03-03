# Structuri repetitive
# WHILE
i = 1
while i <= 101:
    print(f'Dalmatianul curent este {i}')
    i = i + 1

# in sens invers
i = 101
while i >= 1:
    print(f'Dalmatianul curent este {i}')
    i = i - 1

# afisarea fiecarei litere dintr-un cuvant
cuvant = 'strugure'
c = 0
while c < len(cuvant):
    print(cuvant[c])
    c = c + 1
print('.......................................')

lista = [1, 35, 40, 'Deea', 3.14, True, 88, 35, False, 'Razvan']
i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1

# FOR
# afisare toate nr de la 1 la 101, se ia in calulc 102-1
for x in range(1,102, 1):
    print(f'Dalmatianul curent este {x}')

for x in range(1,10):
    print(f'Numarul curent este {x}')

# din 2 in 2, ne arata nr de la 1 la 9 inclusiv
for x in range(1,10, 2):
    print(x)

# nr de la 10 la 1, invers
for x in range(10,0, -1):
    print(x)
print('.......................')

# parcurgerea listei cu for - x un index
for x in range(0, len(lista)):
    print(lista[x])
print('.......................')

# FOR EACH
# x este fiecare element din lista; nu mai este un index ca si la FOR
for x in lista:
    print(x)
print('........................')

dict = {'Nume': 'Zegrean', 'Prenume': 'Andreea'}
for x in dict:
    print(x)
for x in dict.values(): # ne ajuta sa accesam valorile din dictionar
    print(x)
print('........................')

tuplu = (1, 2, 3, 'Maria', True, 5.12)
for x in tuplu:
    print(x)
print('........................')

# la seturi ordinea nu se pastreaza, nu sunt elemente ordonate
set = {'Andreea', False, 77, 36, True, 9.9}
for x in set:
    print(x)
print('........................')

lista_fructe = ['Ananas', 'Rosii', 'Cirese', 'Mere', 'Kiwi', 'Banane']
for x in lista_fructe:
    if x == 'Cirese':
        print('Am ajuns la cirese, deci ne oprim')
        break # se opreste brust la cirese
    print(x)
print('........................')

for x in lista_fructe:
    if x == 'Cirese':
        print('Ciresele - Fructele din lista')
        continue # citeste toata lista, sarind peste cirese
    print(x)
print('........................')

i = 1
while i < 10:
    if i == 2:
        break
    print(i)
    i = i + 1
print('........................')

i = 0
while i < 10:
    i = i + 1
    if i == 2:     # parcurgem toate nr fara 2
        continue
    print(i)


