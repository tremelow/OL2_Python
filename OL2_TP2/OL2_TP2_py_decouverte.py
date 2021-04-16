# -*- coding: utf-8 -*-

x, y = 2, 0 # initialisation de 2 variables
p = (y >= -4)
q = (x <= 3)

p & q  # ET logique
p | q  # OU logique
not(p) # NON logique

x & y # ET par bit
x | y # OU par bit
~x    # NON par bit

y == 4 # égalité
y != 4 # différence