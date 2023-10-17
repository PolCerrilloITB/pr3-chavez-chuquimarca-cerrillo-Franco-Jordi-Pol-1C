'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
17/10/2023
ASIXc1C M03 UF1
Descripció:Escriu un programa que llegeixi 5 enters.
El primer i el segon creen un rang, el tercer i el quart creen un altre rang.
Mostra True si el cinquè valor, està comprès dins els dos rangs, si no False.
'''
#Els extrems dels rangs inclosos, el primer rang

primervalor=int(input("1r enter: "))
segonvalor=int(input("2n enter: "))
tercervalor=int(input("3r enter: "))
quartvalor=int(input("4t enter: "))
cinquevalor=int(input("5è enter: "))

primrang=(primervalor <= cinquevalor <= segonvalor)
segrang=(tercervalor <= cinquevalor <= quartvalor)

if primrang and segrang:
    print("True")
else:
    print("False")
