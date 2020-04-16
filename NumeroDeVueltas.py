#Programa capaz de calcular el número de vueltas de una llanta en 1 km

print("Programa que calcula el número de vueltas de una llanta en 1Km")

print("Primero debemos calcular cuantas vueltas dara la llanta en un diametro de 50cm")

V = 3.1416 * 50

print("La llanta da", V ,"vueltas")

print("Ahora debemos homologar las medidas")

M = (V/100000)

print(M)

print("Por ultimo hallar la cantidad de vueltas que da la llanta")

Vu = (1/M)

print("La cantidad de vueltas que da la llanta son:", Vu)