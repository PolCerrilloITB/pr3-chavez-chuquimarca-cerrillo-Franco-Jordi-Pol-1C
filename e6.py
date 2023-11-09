'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
9/1/2023
ASIXc1C M03 UF1
Descripció: L'usuari introdueix la lletra del tipus d'habitatge i número de m3  d'aigua gastats.
Mostrar per pantalla el preu total de la factura de l’aigua. Arrodonit a 2 decimals
'''

tipo = input()
m3 = float(input())

# Variables definides

precioFijo = 0
precio = 0

# Tipus definits amb el seu preu definit

if tipo == "A":
    precioFijo = 2.40
elif tipo == "B":
    precioFijo = 6.40
elif tipo == "C":
    precioFijo = 7.25
elif tipo == "D":
    precioFijo = 11.21
elif tipo == "E":
    precioFijo = 12.10
elif tipo == "F":
    precioFijo = 17.28
elif tipo == "G":
    precioFijo = 28.01
elif tipo == "H":
    precioFijo = 40.50
elif tipo == "I":
    precioFijo = 61.31

# m3 definides amb els corresponents calculs

if m3 == [0-6]:
    precio = m3*0.5849
elif m3 == [7-9]:
    precio = m3*1.1699
elif m3 == [10-15]:
    precio = m3*1.7548
elif m3 == [16-18]:
    precio = m3*2.3397
elif m3 > 18:
    precio = m3*2.9246

precioTotal = (m3 * precio) + precioFijo
precioTotal = round(precioTotal,2)
print(precioTotal)

