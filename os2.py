import os
katalog=os.getcwd()
print (katalog)


lista=os.listdir(katalog)
print(lista)

katalogdoszukania="/home/uczen/PycharmProjects/JZ/"
lista=os.listdir(katalogdoszukania)
pary=[]
for plik in lista:
    gdzie=os.path.join(katalogdoszukania, plik)
    rozmiar=os.path.getsize(gdzie)
    pary.append((plik, rozmiar))
suma=0
for para in pary:
    print(para)
    suma+=para[1]

print(suma)