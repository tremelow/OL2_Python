# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


m, g, Vmax = 80, 9.81, 200/3.6
k2 = m*g/(Vmax**2)

def f(t,v):
    return g * (1.0 - (v/Vmax)**2 ) # oui j'ai simplifié l'expression

def sol_ex(t):
    return Vmax * np.tanh(g*t/Vmax) # oui, j'ai aussi calculé la sol exacte

def euler(y0, t0, tN, N):
    h = (tN - t0)/N
    t = np.linspace(t0, tN, N+1)
    
    y = [y0]
    for n in range(N):
        y.append(y[n] + h*f(t[n], y[n]))
        
    return t,y

y0, t0, tN = 0.0, 0.0, 40.0
t_ex = np.linspace(t0, tN, 201)
y_ex = sol_ex(t_ex)

for N in [10, 30, 50]:
    t, y  = euler(y0, t0, tN, N)
    
    plt.figure()
    plt.plot(t_ex, y_ex, label="sol. ex.", color="purple")
    plt.scatter(t, y, label="N = " + str(N), marker="x")
    plt.legend()




## Vitesse limite 190 km/h, méthode graphique
Vlim = Vmax * 0.95

plt.figure()
plt.plot(t_ex, y_ex, label="sol. ex.", color="purple")
plt.plot([t0, tN], [Vlim, Vlim], label="190 km/h", 
     linestyle="dashed", color="gray")
plt.legend()


## Méthode non graphique
h = 1e-4 # précision
tn, yn = t0, y0
while yn <= Vlim:
    yn += h*f(tn, yn)
    tn += h

print("Temps pour atteindre 190 km/h : %.4f s." % tn)