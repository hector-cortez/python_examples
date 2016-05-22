# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado tres números A, B, C determinar y desplegar cual es el mayor.
'''
a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo número: "))
c = int(input("Introduzca el tercer número: "))

if a > b:
    if a > c:
        print a, " es el mayor"
    else:
        print c, " es el mayor"
else:
    if b > c:
        print b, " es el mayor"
    else:
        print c, " es el mayor"

