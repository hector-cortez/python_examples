# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado un número N determinar si es cuadrado perfecto,
N: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
desplegar si es o no perfecto.
'''
n = int(input("Introduzca un número: "))
x = 1
while n > x * x:
    x += 1

if (x * x) == n:
    print n, "Es un Cuadrado Perfecto"
else:
    print n, "No es un Cuadrado Perfecto"
