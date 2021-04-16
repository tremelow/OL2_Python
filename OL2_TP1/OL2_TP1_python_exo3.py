# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


v1 = np.arange(-4, 15) # le pas est 1 par défaut
v2 = np.arange(-2, 2, 1/100)

print("Le vecteur v2 contient", len(v2), "éléments.")
# /!\ On indice à partir de 0 !
print("Son 30ème élément est ", v2[29], ".", sep='') # [1]
# syntaxe pour le dernier élément
print("Son dernier élément est ", v2[-1], ".", sep='')


v3 = np.linspace(1,8, 20) # comme en Scilab

print("Les 7 premiers éléments de v3 : ")
print(v3[:7])


x = np.linspace(0.5, 2.0, 100) 
lnx = np.log(x)
y = x - 1 

# affichage avec la légende donnée séparément dans chaque courbe
plt.plot(x, lnx, color="blue", label="ln(x)")
plt.plot(x, y, color="red", label="x+1")
plt.legend() # il faut quand même préciser qu'on veut une légende
plt.xlabel("x")

plt.show()


# [1] https://realpython.com/python-print/#printing-in-a-nutshell
# pour comprendre la syntaxe "sep"