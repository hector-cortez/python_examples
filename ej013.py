# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado un numero real R, intercambiar la parte entera por la parte decimal,
Desplegar ambos números.
'''
nroReal = float(input("Introduzca un número(Real): "))
# Separamos la parte entera de la parte decimal utilizando la funcion parte entera
entera = int(nroReal)
# Multiplicamos de forma  sucesiva por 10 hasta que la parte parte decimal sea 0.
realTemp = nroReal -  entera
parteDecimal = 0
while int(realTemp) != realTemp:
    realTemp = realTemp * 10
    parteDecimal = int(realTemp) * 10
print entera
print parteDecimal
