# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado un numero X determinar si es un número primo, desplegar en número y el mensaje.
'''
"""
x = int(input("Introduzca un número: "))
cde = 0
for d in range(1, x + 1, 1):
    if (x // d) * d == x:
        cde += 1
        print "es div"
print cde
if cde == 2:
    print x, " es primo"
else:
    print x, " no es primo"
"""

x = int(input("Introduzca un número: "))
cde = 0
for d in range(2, x, 1):
    if (x // d) * d == x:
        cde += 1
        break
        print "es div"
print cde
if cde != 0:
    print x, " no es primo"
else:
    print x, " es primo"
