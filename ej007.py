# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado un número A determinar si es par o impar, mediante restas sucesivas.
desplegar el número y el mensaje. 
'''
n = int(input("Introduzca un número: "))
m = n
while n >= 2:
    n -= 2
if n == 0:
    print m, " es par"
else:
    print m, " es impar"

