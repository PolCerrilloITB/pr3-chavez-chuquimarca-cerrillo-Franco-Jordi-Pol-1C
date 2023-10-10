'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
10/10/2023
ASIXc1C M03 UF1
Descripció: Calcula el volum de l'aula
'''
#Calcula el volum de l'aula i imprimeix per pantalla el resultat de la operació.

longitud = int(input("Longitud de l'aula en metres?"))
anchura = int(input("Anchura de l'aula en metres?"))
altura = int(input("Altura de l'aula en metres?"))

volumen = longitud*anchura*altura

print("El volumn de l'aula és", volumen,"m³")