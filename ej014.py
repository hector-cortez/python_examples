# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado un número X hallar su cuadrado con la suma de sus X numeros impares,
desplegar los números impares y su cuadrado.
'''
import sys

x = int(input("Introduzca un número: "))

imp = 1
cx = 0
for ca in range(1, x + 1, 1):
    cx = cx + imp
    sys.stdout.write(str(imp) + " ")
    imp += 2

print "\nLa suma de impares", cx
