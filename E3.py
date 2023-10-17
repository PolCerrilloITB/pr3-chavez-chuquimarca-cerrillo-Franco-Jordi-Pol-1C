'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
17/10/2023
ASIXc1C M03 UF1
Descripció:Escriu un programa que llegeixi 5 enters.
El primer i el segon creen un rang, el tercer i el quart creen un altre rang.
Mostra True si el cinquè valor, està comprès dins els dos rangs, si no False.
'''
#Els extrems dels rangs inclosos, el primer rang

primerValor=int(input("1r enter: "))
segonValor=int(input("2n enter: "))
tercerValor=int(input("3r enter: "))
quartValor=int(input("4t enter: "))
cinqueValor=int(input("5è enter: "))

primRang=(primerValor <= cinqueValor <= segonValor)
segRang=(tercerValor <= cinqueValor <= quartValor)

if primRang and segRang:
    print("True")
else:
    print("False")
