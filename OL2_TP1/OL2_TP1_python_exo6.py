# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


w = np.linspace(-50, 50, 10001)
Z = 1j*w / (1 + 2j*w) # racine de -1 : 1j

plt.plot(Z.real, Z.imag)
plt.axis("equal") # repère orthonormé
