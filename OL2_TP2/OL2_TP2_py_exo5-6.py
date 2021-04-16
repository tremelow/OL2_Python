# -*- coding: utf-8 -*-

import numpy as np


#-------------------------------
# Exo 5

n, p = 20, 20 # nombre de lignes et de colonnes
A = np.matrix([[0]*p]*n)

for i in range(n):
    for j in range(p):
        if i == j:
            A[i,j] = 1
        elif i < j:
            A[i,j] = 2
        else:
            A[i,j] = 3
        # ou bien, mais moins clair
        A[i,j] = 1 if i == j else 2 if i < j else 3
        
# en une ligne:
A = [[3]*i + [1] + [2]*(p-i-1) for i in range(n)]
# on peut convertir en matrice numpy
A = np.matrix(A)

print(A)


#------------------------------
# Exo 6

taux = 1.25/100
capital_initial = 1000
capital = capital_initial

profits = 100
annee = 0

while capital <= capital_initial + profits:
    capital *= 1 + taux
    # pour tronquer au centime près:
    capital = np.floor(capital*100)/100
    annee += 1

print("Après %d années, les profits ont dépassé %d€" %(annee, profits),  
      "et le capital atteint %.2f€." %capital)