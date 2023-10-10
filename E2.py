'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
10/10/2023
ASIXc1C M03 UF1
Descripció: Calcula el volum de l'aula
'''
#Calcula el volum de l'aula i imprimeix per pantalla el resultat de la operació.

longitud = int(input("Longitud del aula en metros?"))
anchura = int(input("Anchura del aula en metros?"))
altura = int(input("Altura del aula en metros?"))

volumen = longitud*anchura*altura

print("El volumen del aula es", volumen,"m³")