# -*- coding: utf-8 -*-

#----------------------------
# PROGRAMME DE BASE

print("Donner un nombre positif strictement supérieur à 1, x = ", end='')
x = float(input())

Max = 10**6 # /!\ 10^6 == 12 (OU par bit)
n = 1

while x**n <= Max:
    n += 1
    
print("La valeur de ", x, "^", n, " est ", x**n, sep='')


#----------------------------
# PROGRAMME MODIFIÉ

x = float(input("Donner un nombre compris entre -1 et 1, x = "))
assert abs(x) < 1

n = 1
eps = 10**-6
while abs(x**n) > eps:
    n += 1
    
print("La valeur de ", x, "^", n, " est ", x**n, sep='')
