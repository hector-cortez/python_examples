# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Leer un número entero X y desplegar su valor absoluto.
'''
import math
a = int(input("Introduzca el primer número(A): "))
b = int(input("Introduzca el segundo número(B): "))
if a > b:
    c = a - b
else:
    c = b - a
print "Resultado:", c
