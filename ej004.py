# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dados dos números A y B, hallar su producto por sumas sucesivas, almacenar el resultado en la variable P.
'''
import math
a = int(input("Introduzca el primer número(A): "))
b = int(input("Introduzca el segundo número(B): "))
p = 0
for c in range(b):
    p = p + a

print "Resultado:", p
