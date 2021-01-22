# -*- coding: utf-8 -*-
#Change Figure size
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
plt.scatter(x,y)
# get reference to the current figure
fig = plt.gcf()
fig.set_size_inches(8,3)
plt.show()
