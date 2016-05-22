# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
El la expresión A + X = B, dados los valores de A y B hallar el valor de X sin realizar 
la operacion de resta X = B - A, desplegar X.
'''
a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo número: "))
x = 0
while (a + x) != b:
    if a > b:
        x -= 1
    else:
        x += 1

print "El valor de X es:", x
