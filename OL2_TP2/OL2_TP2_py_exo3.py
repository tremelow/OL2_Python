# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 601)

#------------------------------
# HEAVISIDE

# Boucle v1
y = []
for i in range(len(x)):
    if x[i] > 0:
        y.append(1)
    else:
        y.append(0)


# Boucle v2
y = [0 for _ in x]
for (i, xi) in enumerate(x):
    y[i] = (1 if xi > 0 else 0)

# Vectoriel v1
y_bool = x > 0 # booléens
y = y_bool.astype(float) # ou int

# Vectoriel v2
y = (x > 0).astype(float)

# Vectoriel v3
y = (x > 0) * 1.0

plt.plot(x,y, label="échelon")


#-----------------------------
# TRIANGLE

# v1
y = (1 - abs(x)) * ((x > -1) & (x <= 1))

# v2
y = (x + 1) * ((x > -1) & (x <= 0)) + (1 - x) * ((x > 0) & (x <= 1))

plt.plot(x,y, label="triangle")
plt.legend()
plt.show()