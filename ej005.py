# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Calcular el factorial de un número N, mostrar el número y su factorial.
'''
n = int(input("Introduzca un número: "))
factorial = 1
for c in range(n):
    factorial *=  (c + 1)

print "Factorial:", factorial