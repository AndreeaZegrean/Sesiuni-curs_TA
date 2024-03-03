cuvant = 'ITFactory'
print(cuvant[0:9])  # parcurge toate caracterele
print(cuvant[0:9:1])  # parcurge toate caracterele
print(cuvant[0:9:2])  # din 2 in 2
print(cuvant[0:9:3])  # din 3 in 3
print(cuvant[1:4:2])  # de la poz 1 pana la poz 4, din 2 in 2
print(cuvant[2])  # un singur caracter
print(cuvant[-1])  # doar ultima litera din cuvant
print(cuvant[::-1])  # cuvantul se scrie invers
print(cuvant[9:0:-1])  # cuvantul se scrie invers fara prima litera
print(cuvant[::])  # vrem sa fie parcurs normal si ne arata tot cuvantul

cuvant2 = cuvant[::]  # copie a variabilei initiale
print(cuvant2)

print(cuvant[:5:])  # parcurge pana la pozitia 5 inclusiv, numeroatrae incepe de 0
print(cuvant[1::])  # parcurge tot fara poz 1, adica fara T

x = 50.27
print(str(x)[0:2])  # ne arata doar partea intreaga

y = 'Georgescu'
# va inlocui doar g cu 7 (g cu litera mica)
print(y.replace('g', '7'))
# transforma toate litere in litere mici, dar si inlocuieste (replace)
print(y.lower().replace('g', '7'))
# transforma toate litere in litere mari, dar si inlocuieste (replace)
print(y.upper().replace('G', '7'))
# transforma toate litere in litere mari, dar si inlocuieste (replace), apoi le face litere mici
print(y.upper().replace('G', '7').lower())
print(y.upper())  # transforma in litere mari
print(y.lower())  # transforma in litere mici

z = 'Ana are Mere'
# split - imparte in sectiuni separate cand intalneste lit a
print(z.split('a'))

z = 'Ana are Mar'
print(z.split('a'))  # face bucatele mai mici and intalneste lit a

b = 'Ana.are.Mar'
print(b.split('.'))
print(b.split('r'))

print(b.index('A'))  # ne returneaza poz unui caracter din string
print(b.index('.'))  # ne returneaza poz caracterului ' . ' = 3

print(b.islower())  # returneaza true daca este construit doar din litere mici
nume = 'ana'
print(nume.islower())  # returneaza true fiind cu litere mici
nume = 'ANA'
print(nume.isupper())  # returneaza true fiind cu litere mari

nume = 'popescu'
print(nume.capitalize())  # ne transforma prima litera in litera mare

print(nume.count('p'))  # de cate ori se afla litera p in cuvant
print(len(nume))  # lungimea caracterului
print(nume[0:len(nume)])  # printeaza tot stringul
print(nume[0:12])  # printeaza tot indiferent de dimensiu daca este mai scurt
# print(nume[12]) - nu avem caracter pe indexul 12, deci ne returneaza eroare

telefon = '07283456775'
# returneaza true daca contine carcatere de la 0 la 9
print(telefon.isdecimal())
telefon = 'A1234B'
# returneaza false daca contine alte carcatere in afara de cifre
print(telefon.isdecimal())

# returneaza true daca contine carcatere la putere, exponent
x = "2²"
print(x.isdigit())
# returneaza false daca contine carcatere in afara de cifre
print(x.isdecimal())

# returneaza true daca contine carcatere ca si fractie
x = "¾"
print(x.isnumeric())
# returneaza false daca contine carcatere in afara de cifre
print(x.isdecimal())
print(x.isdigit())
