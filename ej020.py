# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado dos numeros a y b enteros mayores a cero, hallar a^b en base a sumas sucesivas.
Desplegar los números y el resultado.
'''
a = int(input("Introduzca un número: "))
b = int(input("Introduzca un número: "))

p = 1
sp = 0

for cb in range(1, b + 1, 1):
    for ca in range(1, a + 1, 1):
        sp = sp + p
    p = sp
    sp = 0

print a, b, p
