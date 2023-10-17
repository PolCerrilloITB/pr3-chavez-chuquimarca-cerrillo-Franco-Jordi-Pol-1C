"""
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
10/10/23
ASIXc1C M03 UF1
Descripcion:Demanar el diàmetre d'una pizza rodona i imprimeix la seva superfície.
Pots usar Math.PI per escriure el valor de Pi.
"""
#Calcula la superfície de la pizza y pon el resultado en pantalla
import math

diametro = int(input("¿Cual es el diametro de la pizza en centimetros?"))
PI = math.pi
superficie = (diametro/int(2))**int(2)*PI
print("Tu pizza tiene una superficie de",str(superficie),"cm²")
