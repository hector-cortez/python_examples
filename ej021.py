# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado tres numeros enteros mayores a cero A, B y C, hallar (A^B)^C por sumas sucesivas.
Desplegar los numeros y el resultado.
'''
a = int(input("Introduzca número A: "))
b = int(input("Introduzca número B: "))
c = int(input("Introduzca número C: "))

p = 1
sp = 0
for cb in range(1, b + 1, 1):
    for ca in range(1, a + 1, 1):
        sp = sp + p
    p = sp
    sp = 0
pr = 1
sp = 0
for cc in range(1, c + 1, 1):
    for cp in range(1, p + 1, 1):
        sp = sp + pr
    pr = sp
    sp = 0
print a, b, c, pr
