"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
7/1/2023
ASIXc1C M03 UF1
Descripcion: Programa que demana dos números si el primer és més gran o igual que el segon els intercanvia.
I torna a mostrar els valors per pantalla
"""
# Introduim un .split() per tenir un espai entre numeros

num1, num2= (input("Dos numeros? ").split())

# Variables dels numeros

num1 = int(num1)
num2 = int(num2)

# Orientació dels numeros segons el seu valor

if num1 == num2 or num1 > num2:
    num1 = num2
    num2 = num1
    print(num1, num2)

else:
    print(num1, num2)
