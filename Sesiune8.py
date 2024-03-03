# Concepte de abstractizare
from abc import ABC, abstractmethod

# clasa parinte cu 2 metode abstracte
class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        print('Buna ziua')

    @abstractmethod
    def ora_de_somn(self):
        print('somn usor')

# snake case pt metode/atribute/nume de fisiere
# camel case pt nume de clase

# clasa copil mosteneste din clasa parinte Gradinita
class GradinitaPublica(Gradinita):
    def nr_gradinita(self):
        print('Suntem in gradinita publica')
    # prin suprascriere oferit un comportament diferit in clasa copil
    def activitate_practica(self):
        print('copii invata sa deseneze')
    def ora_de_somn(self):
        print('copii trebuie sa doarma la ora 17:00')

class GradinitaPrivata(Gradinita):
    def activitate_practica(self):
        print('copii se joaca')
    def ora_de_somn(self):
        print('copii dorm la pranz')

# Encapsularea
class GradinitaPublica25(GradinitaPublica):
# definire atribute
    atribut_public = 'Atribut Public'
    _atribut_protected =  'Atribut Protected'
    __atribut_private = 'Atribut Private' # nu se poate accesa din interiorul clasei

    # Proprietatile ghetter, setter, deleter
    @property # ghetter
    def atribut_privat(self):
        return self.__atribut_private

    # se poate atribui o noua valoare, doar in clasa ai acces la atributul privat
    @atribut_privat.setter
    def atribut_privat(self, new):
        self.__atribut_private = new
    @atribut_privat.deleter
    def atribut_privat(self):
        del self.__atribut_private
# instantiere obiect, punem numele clasei de unde vrem sa-l instantiem
gradinita_publica = GradinitaPublica()
gradinita_publica.ora_de_somn()

gradinita_privata = GradinitaPrivata()
gradinita_privata.activitate_practica()

gradinita_publica25 = GradinitaPublica25()
print(gradinita_publica25.atribut_public)
print(gradinita_publica25._atribut_protected)
# print(gradinita_publica25.__atribut_private) - da eroare

print(gradinita_publica25.atribut_privat) # ghetter
gradinita_publica25.atribut_privat = 'new 777' # setter
print(gradinita_publica25.atribut_privat)
del gradinita_publica25.atribut_privat # del - sterge noua valoarede la linia 65
print(gradinita_publica25.atribut_privat)

# Polimorfism
# metode cu aceleasi nume in clase diferite

class America():
	limba = "Engleza"
	drapel = "American"
	imn = "Imnul americii"

	def printeaza_limba(self):
			print(f"Limba care se vorbeste in america este {self.limba}")

class Romania():
	limba = "Romana"
	drapel = "tricolor"
	imn = "desteapta-te romane"

	def printeaza_limba(self):
			print(f"Limba care se vorbeste in romania este {self.limba}")

obiect_america = America()
obiect_romania = Romania()
obiect_romania.printeaza_limba()
obiect_america.printeaza_limba()

class Casa_encapsulare:
		# decorator = elemente care modifica comportamentul unei functii
		_numar_etaje = None
		numar_camere = None
		numar_bai = None
		__material_constructie = None
		suprafata = None
		an_constructie = None
		adresa = None
		clasa_energetica = None
		pret = None

		def __init__(self, numar_etaje, numar_camere, numar_bai, material_constructie, suprafata, adresa):
				self._numar_etaje = numar_etaje
				self.numar_camere = numar_camere
				if numar_bai > 2:
						print("Nu putem construi mai mult de doua bai")
				else:
						self.numar_bai = numar_bai
				self.__material_constructie = material_constructie
				self.suprafata = suprafata
				self.adresa = adresa

		def calculeaza_aprobare_numar_etaje(self):
				if self.numar_etaje > 5:
						print("Apartamentul are mai mult de 5 etaje, drept urmare se poate acorda aprobarea necesara")
				else:
						self.aprobare = True

		def __actualizeaza_an_constructie(self, an_constructie):
				self.an_constructie = an_constructie
				return self.an_constructie

		def vinde_casa(self):
				print(f"Apartament de vanazare in zona lalelelor"
							f"Numar camere: {self.numar_camere}"
							f"Numar etaje: {self._numar_etaje}"
							f"Numar bai: {self.numar_bai}"
							f"An constructie: {self.an_constructie},"
							f"Suprafata: {self.suprafata}"
							f"Material constructie: {self.__material_constructie}")

		@property
		def materiale_constructie(self):
				pass

		@materiale_constructie.getter
		def materiale_constructie(self):
				return self.__material_constructie

		@materiale_constructie.setter
		def materiale_constructie(self, material_constructie):
				self.__material_constructie = material_constructie

		@materiale_constructie.deleter
		def materiale_constructie(self):
				self.__material_constructie = None


garsoniera = Casa_encapsulare(0, 1, 1, "beton", 40, "Strada Lalelelor 23")
print(f"materiale de constructie returnate prin getter inainte de update: {garsoniera.materiale_constructie}")  # apelare getter
garsoniera.materiale_constructie = "caramida"  # setter
print(f"materiale de constructie returnate prin getter dupa update: {garsoniera.materiale_constructie}")  # apelare getter
del garsoniera.materiale_constructie
print(f"materiale de constructie returnate prin getter dupa delete: {garsoniera.materiale_constructie}")  # apelare getter