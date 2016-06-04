# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Evaluar la expresión tx = (x^2 + 10)/sqrt(a - x)
Para a que se lee como dato de entrada, x = 1, 1.5, 2, 2.5, ..., 10
Desplegar a, x, tx
'''
import math
a = int(input("Introduzca un número: "))
x = 1
while x <= 10:
    num = (x ** 2) + 10
    if (a - x) > 0:
        den = math.sqrt(a - x)
        tx = num / den
        print a, x, tx
    else:
        print 'No hay solución, raiz cuadrada negativa.'
    x = x + 0.5
