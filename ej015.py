# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado los valores A, B, C que son coeficientesde la ecuación de segundo grado,
hallar sus raices reales, desplegar los resultados.
'''
import math

a = int(input("Introduzca un valor de A: "))
b = int(input("Introduzca un valor de B: "))
c = int(input("Introduzca un valor de C: "))

disc = (b * b) - (4 * a * c)

if disc > 0:
    rc = math.sqrt(disc)
    x1 = (-b + rc)/(2 * a)
    x2 = (-b - rc)/(2 * a)
    print x1, x2
elif disc == 0:
    x1 = (-b)/(2 * a)
    x2 = x1
    print x1, x2
else:
    print 'No existen raices reales' 
