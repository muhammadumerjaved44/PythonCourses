# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
plt.plot(x,y)
# rotating labels on the xaxis
plt.xticks(rotation=60)
# y axis
plt.yticks(rotation=60)
