'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
9/1/2023
ASIXc1C M03 UF1
Descripció: Programa que comprovi si una data és correcte.
El programa ha de demanar una data, dia, mes i any (en el format DD/MM/AAAA).
Cal recordar que hi ha anys de traspàs
'''

# Dia/mes/any els transformem a int i els fiquem a las seves variables

dia, mes, any = input("Dia/mes/any: ").split("/")
dia = int(dia)
mes = int(mes)
any = int(any)

# Amb els if i els elif, fem la comprovació dels respectius dias mesos i anys.

if mes == 1 | 3 | 5 | 7 | 8 | 10 | 12:
    if dia > 0 and dia <= 31:
        print("data correcte")
elif mes == 4 | 6 | 9 | 11:
    if dia > 0 and dia <= 31:
        print("data correcte")
elif mes == 2:
    if any % 4 == 0:
        if dia > 0 and dia <= 29:
            print("data correcte")
        else:
            print("data incorrecte")
    elif dia > 0 and dia <= 28:
        print("data correcte")
    else:
        print("data incorrecte")
else:
    print("data incorrecte")
