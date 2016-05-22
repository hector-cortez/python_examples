# -*- coding: utf-8 -*-
'''
@author: Hector Cortez
Dado dos numeros A y B realizar la división entera por restas sucesivas, 
desplegar los números, el cociente y el residuo.
'''
a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo número: "))
residuo = a
cociente = 0
while residuo >= b:
    residuo -= b
    cociente += 1
print "Primer número: ", a
print "Segundo número: ", b
print "Cociente:", cociente
print "Residuo", residuo 


