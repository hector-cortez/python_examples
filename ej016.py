# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado el valor A, evaluar la expresión Y = X^2 + A, para los valores de x = 1,2,3,...10.
Desplegar A, X y el resultado Y
'''

a = int(input("Introduzca un número: "))

for x in range(1, 11, 1):
    y = x * x - a
    print a, x, y
