# -*- coding: utf-8 -*-

"""
     ATTENTION:                                        
En Python, pas de moyen de nettoyer la mémoire automatiquement, il faudra 
faire attention à exécuter les scripts de façon isolée.
"""


########################################
## IMPORT DES LIBRAIRIES (ou packages)

# syntaxe "import package as alias" permet d'appeler les fonctions comprises
# dans package en faisant alias.fonction().


## NUMPY:
# permet les opérations vectorielles. Fourni le type "numpy.array" qui 
# comprend les opérations standards (+,-,*,/) terme à terme. Les opérations 
# par défaut *ne sont pas* les opérations vectorielles. Pas de distinction
# entre vecteurs lignes ou colonnes.
import numpy as np

## PYPLOT:
# pour les affichages de graphes
import matplotlib.pyplot as plt


x = np.arange(-2, 1.5, 0.1) # fonction numpy, -2 : 0.1 : 1.5 en Scilab

y1 = np.exp(x) # Python ne connait pas exp par défaut
y2 = (2 + x) / (2 - x) # /!\ pas terrible pour la rigueur : avec numpy, la
                       # multiplication se fait automatiquement terme à terme
y3 = x + 1

print("Il y a", len(x), "éléments dans le vecteur x.")

# Affichages graphiques un peu comme en Scilab
plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="red")
plt.plot(x, y3, color="green")

plt.xlabel("x") # légende de l'axe des abscisses

plt.legend(["exp(x)", "(2+x)/(2-x)", "x+1"])
plt.title("Tracé de trois courbes sur le même graphe avec titre et légende")
plt.grid()

plt.show() # en fonction de l'environnement utilisé (pas besoin avec Spyder)
