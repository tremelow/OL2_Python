# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-80, 120, 1001)

y1 = (x - 20) * (x + 60) * (x - 100)
y2 = -y1

plt.plot(x, y1, color="blue", label="(x-20)(x+60)(x-100)")
plt.plot(x, y2, color="green", label="-(x-20)(x+60)(x-100)")
plt.legend()
plt.xlabel("x")

plt.show()