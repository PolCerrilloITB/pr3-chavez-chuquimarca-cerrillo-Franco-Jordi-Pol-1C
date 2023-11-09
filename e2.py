'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
7/1/2023
ASIXc1C M03 UF1
Descripció: Programa que detecta si tres números demanats han estat introduïts en ordre creixent.
'''

# separació dels numeros amb el .split()

num1, num2, num3 = (input("Tres numeros:").split())

# pasar els numeros a int

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

# ordre dels numeros segons el seu valor

if num1 < num2 and num2 < num3:
    print("Ordre creixent")
else:
    print("Barreja")