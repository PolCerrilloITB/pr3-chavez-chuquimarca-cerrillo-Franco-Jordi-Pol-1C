'''
Franco Chavez/Jordi Chuquimarca/Pol Cerrillo
7/1/2023
ASIXc1C M03 UF1
Descripció: Programa que demana l'import d'una factura, amb iva inclòs.
Calcula l'import amb descompte, en cas de tenir la targeta de client,
tenint en compte els següents criteris:
'''
pTotal0 = int(input(print("Cual es el precio total de lo pagado, con el iva incluido?")))

# calcul de la variable dins del if

if pTotal0 >= 100:
    pInicial = pTotal0*0.79
    Descuento = pInicial*1.21
    print("El precio con el descuento es de ",round(Descuento,2),"€")
else:
    print("No se aplica el descuento")