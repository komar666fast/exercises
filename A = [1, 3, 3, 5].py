# A = [1, 3, 3, 5]
# wynik = list(set(A))
# print(wynik)
# A[-2]

# # for a in range(2,9):
# #     print(a)

# def sum(a, b = 3):
#   wynik = a + b
#   return wynik

# print(sum(5))


# dict_example = {'a':'alfred', 'b':'borat'}

# print(type(dict_example))
# A.append(10)
# print(A)

# A = []
# B = []
# for i in range(11):
#   A.append(i)
# print('A:', A)

# for i in range(len(A) - 1, -1, -1):
#   B.append(i)
# print('B:', B)

# A.reverse()
# print('Arev:', A)

#gotowa klasa Pojazd

class Pojazd:
    nazwa = ""
    rodzaj = "auto"
    kolor = ""
    wartosc = 100.00
    def opis(self):
        napis_opisu = "%s to %s %s warty %.2f zl." % (self.nazwa, self.kolor, self.rodzaj, self.wartosc)
        return napis_opisu

# Ponizej umiesc swoj kod
Auto1 = Pojazd()
Auto2 = Pojazd()
Auto1.nazwa = 'Ferrari'
Auto1.rodzaj = 'kabriolet'
Auto1.kolor = 'czerwony'
Auto1.wartosc = 60000
Auto2.nazwa = 'Ikarus'
Auto2.rodzaj = 'autobus'
Auto2.kolor = 'niebieski'
Auto2.wartosc = 10000
# sprawdzenie kodu
print (Auto1.opis())
print (Auto2.opis())

class Autobus(Pojazd):
    def __init__(self,wysokosc = 0, ilosc_pasazerow = 0):
        self.wysokosc = wysokosc
        self.ilosc_pasazerow = ilosc_pasazerow
    
    def show(self):
        print('To jest Ikarus!!')

autobus_ikarus = Autobus()
print(autobus_ikarus.wysokosc)
autobus_ikarus.show()

lista1 = [1,2,3]
lista1.append(5)

print(type(lista1))
print(type(autobus_ikarus))

napis = 'Hello world'.split()
print(napis)
print(type(napis))

# split()
# enumerate()
# zip()

even_number = [i for i in range(100) if i % 2 == 0]
print(even_number)

import json

with open('/home/ubuntu/Pictures/data.json', 'r') as file:
    data = json.load(file)

import pprint
print(type(data))
pprint.pprint(data.keys())
# print(data['name'])
for i in data.keys():
    print(data[i])
        