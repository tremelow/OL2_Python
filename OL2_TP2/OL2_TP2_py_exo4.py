# -*- coding: utf-8 -*-

from math import sqrt
import matplotlib.pyplot as plt

#-------------------------------
# INITIALISATION

u0, u1 = 1, 1
n = 15

# v1
u = [u0, u1]
for i in range(n-2):
    u.append(u[i] + u[i+1])

print(*u)

# v2 (sans allocation dynamique de mémoire)
u = [u0, u1] + [0]*(n-2)
for i in range(n-2):
    u[i+2] = u[i] + u[i+1]

print(*u)

# BONUS: en deux ligne avec allocation dynamique
u = [1, 1]
[u.append(sum(u[-2:])) for _ in range(n-2)]

print(*u)


#------------------------------
# QUOTIENTS
u.append(u[-2] + u[-1]) # on rajoute u[n+1]

quots = []
for i in range(n): # /!\ n = len(u) - 1 (le -1 est important)
    quots.append(u[i+1]/u[i])

# BONUS: en une ligne
quots = [u1/u0 for (u0, u1) in zip(u, u[1:])]

plt.plot(quots, marker="x", linestyle="none")


#-------------------------------
# CONVERGENCE

# ma version, sans allouer de tableau

n = 0
u0, u1 = 1, 1
eps = 1e-3
phi = (1 + sqrt(5))/2
while abs(u1/u0 - phi) > eps:
    u0, u1 = u1, u0 + u1 # plus rapide que u2 = u0 + u1 etc
    n += 1

print("Le rapport u[n+1]/u[n] est proche du nombre d'or à ", eps, 
      "près à partir de n = ", n, sep='')
