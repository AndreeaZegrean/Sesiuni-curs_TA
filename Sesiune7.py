# constructor implicit
class Masina:
    marca = 'Toyota'
    an_fabricatie = 2022
    culoare = 'rosie'
    cai_putere = 200
    kilometraj = 0
    def parcurgere_kilometri(self, nr_km):
        self.kilometraj = self.kilometraj + nr_km

# instantiere obiect
masina1 = Masina()
print(masina1.marca, masina1.culoare)

masina2 = Masina()
masina2.culoare = 'albastra'
print(masina2.culoare)

# apelare metoda din clasa
masina2.parcurgere_kilometri(100)
print(masina2.kilometraj)
print(masina1.kilometraj)

class Auto:
# constructor explicit folosit pt a ne ajuta sa personalizam obiectul de la inceput
    def __init__(self, culoare, marca, kilometraj, an_fabricatie, cai_putere):
        self.culoare = culoare
        self.marca = marca
        self.kilometraj = kilometraj
        self.an_fabricatie = an_fabricatie
        self.cai_putere = cai_putere
    def parcurgere_kilometri(self, nr_km):
        self.kilometraj = self.kilometraj + nr_km

masina1 = Auto('verde', 'Audi', 0, 2018, 180 )
print(masina1.culoare, masina1.marca, masina1.an_fabricatie)
masina2 = Auto('galbena', 'BMW', 10,2024, 500)
print(masina2.culoare, masina2.marca)

masina1.parcurgere_kilometri(150)
masina2.parcurgere_kilometri(300)
print(masina1.kilometraj)
print(masina2.kilometraj)

class Caine:
    rasa = 'Akita'
    latrat = 'Ham Ham'
    culoare = 'gri'
    varsta = 3
    talie = 'medie'
    gen = 'femela'
    def sunet(self):
        return f'cainele latra: {self.latrat}'
    def descriere(self):
        return f'{self.rasa} are culoarea {self.culoare} si varsta de {self.varsta} ani '

caine1 = Caine()
print(caine1.sunet())
print(caine1.descriere())

class Animal:
    specie = 'Canina'
    def __init__(self, culoare, rasa, varsta):
        self.culoare = culoare
        self.rasa = rasa
        self.varsta = varsta
    def descriere(self):
        return f'{self.rasa} are cloarea {self.culoare} si varsta de {self.varsta} ani'
    def latra(self):
        return 'ham-ham'

caine1 = Animal('negru', 'husky', 4)
print(caine1.descriere())
print(caine1.latra())
caine2 = Animal('alb', 'pichinez', 2)
print(caine2.descriere())

