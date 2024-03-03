# Structuri de date
# LISTELE = structuri de date care ne permit stocarea mai multor date
# sunt mutabile

lista_1 = [1, 2, 3, 4]
print(lista_1)
lista_2 = [1, 'Ana', 3.2, True]
print(lista_2)

# ne afiseaza elementul din lista, in functie de index ( [2] = 3.2)
print(lista_2[2])

# cate elemente sunt in lista
print(len(lista_2))

# accesam ultimul element din lista
print(lista_2[len(lista_2) - 1])
# penultimul element
print(lista_2[len(lista_2) - 2])

# adaugare element la finalul listei
lista_2.append(35)
print(lista_2)

# adaugare element pe indexul x : nr.6 pe indexul 3
lista_2.insert(3, 6)
print(lista_2)

# stergere elemente din lista, doar primul de acel fel
lista_2.remove(1)
print(lista_2)

# sterge element dupa index
lista_2.pop(4)
print(lista_2)

# sterge ultimul element din lista
lista_2.pop()
print(lista_2)

# SETURI - se definesc cu acolade, nu permite duplicate
# lista neordonata

set_1 = {1, 2, 3, 4, 2}
print(set_1)

# adaugare element - aleatoriu
set_1.add(9)
print(set_1)

# sterge element x din lista
set_1.remove(3)
print(set_1)

# scoate aleatoriu un element din lista
set_1.pop()
print(set_1)

# am transformat lista in set prin casting, dar o face inapoi lista
# am vrut sa scapam de duplicate
lista_3 = [22, 3, 5, 22, 6, 5, 8, 7]
print(list(set(lista_3)))

# TUPLE = pot salva mai multe elemente in aceeasi locatie
# sunt imutabile

tuplu_1 = (77, 9, 35, 23.4, 'Deea', False)
print(tuplu_1)

# putem accesa un element de la indexul dorit
print(tuplu_1[3])

# DICTIONARE = pot salva mai multe elemente de tip cheie valoare
# sunt mutabile
# accesarea elementelor se face pe baza de cheie, nu pe index

# daca sunt mai multe chei cu acelasi nume, il ia pe ultimul
dict_1 = {'Nume': 'Monica', 'Nume': 'Razvan', 'Prenume': 'Asha',
          'varsta': 35,
          'telefon': '0754673489',
          'media_bac': 9.55}
print(dict_1['Nume'])
print(dict_1['varsta'])

# accesare element din dict in dic
dict_2 = {10: 2, 'user_1': 'admin',
          'user_2': {'nume': 'Ale', 'email': 'ale@yahoo.com'}}
print(dict_2['user_2']['nume'])
print(dict_2['user_2']['email'])

# schimbare valoare din dictionar
dict_2.update({'user_2': 'Bogdan'})
print(dict_2)
print(dict_2['user_2'])

# stergere elemente din dictionar
dict_2.pop('user_2')
print(dict_2)

