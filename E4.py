'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
10/10/2023
ASIXc1C M03 UF1
Descripció:Escriu un programa que llegeixi l'edat de
l'usuari i mostri si té edat per treballar, l'edat mínima
per treballar legalment és 16 i suposarem l'edat màxima als 65.
'''

edat = int(input("Quina edat tens?"))

if (edat>=16 and edat<=65):
    print("Pots treballar")
else:
    print("No pots treballar")