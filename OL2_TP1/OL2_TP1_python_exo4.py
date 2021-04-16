# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

A = np.sqrt(2) # np.sqrt fonctionne avec arguments scalaires ou vectoriels
w = 2*np.pi
T = 2*np.pi/w

#   SYNTAXE FONCTION: 
# Attention, Python reconnait qu'on est dans le bloc "def" grâce aux 
# *tabulations*
def I1(t):
    return A*np.sin(w*t)
# fin de la fonction avec return et fin de tabulation

t = np.linspace(0, 3*T, 1001)

y1 = I1(t)
y2 = I1(t - 1/8)

plt.plot(t, y1, color="blue", label="I1")
plt.plot(t, y2, color="red", label="I2")
plt.legend()
plt.xlabel("t")
plt.ylabel("Intensité (en A)")
plt.show()

plt.figure()

y3 = np.exp(-t) * I1(t)
plt.plot(t, y1, color="blue", label="I1")
plt.plot(t, y3, color="green", label="I3")
plt.legend()
plt.xlabel("t")
plt.ylabel("Intensité (en A)")
plt.show()