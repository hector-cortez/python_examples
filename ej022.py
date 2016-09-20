# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Tabla de multiplicar de 1 al 10
'''
for x in range(1, 11, 1):
    for y in range(1, 11, 1):
        z = x * y
        print x, "*", y, "=", z
