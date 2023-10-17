'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
17/10/2023
ASIXc1C M03 UF1
Descripció:Demana una paraula per teclat i mostrar-la per
pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5.
'''
#Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que és el 5.
def reemplaçar_vocals_amb_números(paraula):
    reemplaçament = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5", "A": "1", "E": "2", "I": "3", "O": "4", "U": "5"}
    paraula_modificada = ""
    for lletra in paraula:
        if lletra in reemplaçament:
            paraula_modificada += reemplaçament[lletra]
        else:
            paraula_modificada += lletra
    return paraula_modificada

paraula = input("Introdueix una paraula:")
paraula_modificada = reemplaçar_vocals_amb_números(paraula)
print ("Paraula modificada:" , paraula_modificada)
