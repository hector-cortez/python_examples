# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Evaluar a expresión
tr = (x^3 - 4x + 3)/(x^2 + a)
Para todas las combinaciones de, a = 1,2,3,...,100 y x = 0,1,2,3,...,100
Desplegar a, x, tr
'''

for a in range(1, 20 + 1, 1):
    for x in range(0, 100 + 1, 1):
        numerador = (x ** 3) - (4 * x) + 3
        denominador = (x ** 2) + a
        tr = numerador / denominador
        print a, x, tr
