'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
7/1/2023
ASIXc1C M03 UF1
Descripció: Volem un programa que calculi la velocitat instantània i la velocitat mitjana.
Cal demanar velocitat inicial (m/s), l'acceleració (m/s2) i el temps.
Si la velocitat instantània és inferior o igual a 0, has d'indicar que està parat i no pots
calcular la velocitat mitjana.
'''

# variables de les dades demanades

velocitatInicial = int(input("Velocitat?"))
acceleracio = float(input("Acceleració?"))
temps = float(input("Temps?"))

# creació de noves variables amb els seus calculs

vI = velocitatInicial+acceleracio*temps
vM = (velocitatInicial+vI)/2

# comprobació de si esta aturat el vehicle

if vI == 0 or vI < 0:
    print("El vehicle esta aturat o en direcció negativa i no put calcular la velocitat mitjana")
else:
    print("Velocitat inicial:", vI, "Velocitat mitjana:", vM)