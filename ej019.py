# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Calcular el factorial de un número N por sumas sucesivas,
desplegar el resultado.
'''
n = int(input("Introduzca un número: "))
f = 1
sf = 0
for ca in range(1, n + 1, 1):
    for cs in range(1, ca +1, 1):
        sf = sf + f
    f = sf
    sf = 0

print n, f
