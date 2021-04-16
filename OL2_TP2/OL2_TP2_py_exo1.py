# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 201)

## VERSION 1
y = [] # obligation d'INITIALISER y
for i in range(len(x)):
    y.append(x[i] + np.cos(x[i])) # /!\ cos n'est pas dans Python de base

## VERSION 2
y = [0] * len(x)
for (i, xi) in enumerate(x):
    y[i] = xi + np.cos(xi)

## VERSION 3
y = x + np.cos(x)

plt.plot(x, y)
plt.show()


## Somme des éléments de x
# boucle
s = 0
for xi in x:
    s += xi

# sans boucle
s = sum(x) # rq: fonction de base de Python

print(s)