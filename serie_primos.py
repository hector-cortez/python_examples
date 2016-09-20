# -*- coding: utf-8 -*-
# Serie de los n numeros primos

def nroPrimo(x):
    cde = 0
    for d in range(2, x, 1):
        if (x // d) * d == x:
            cde += 1
            break
    return cde

x = int(input("Introduzca un número: "))
for nro in range(1, x + 1, 1):
    if nroPrimo(nro) == 0:
        print nro
