# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado los laods A, B, C de un triángulo cualquiera, hallar y desplegar su área.
'''
import math
a = int(input("Introduzca valor de A: "))
b = int(input("Introduzca valor de B: "))
c = int(input("Introduzca valor de C: "))

s = (a + b + c)/2
r = s * (s - a) * (s - b) * (s - c)
if r > 0:
    area = math.sqrt(r)
    print "area: ", area
else:
    print "No hay area"

