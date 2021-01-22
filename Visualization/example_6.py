# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
plt.scatter(x,y)
# get reference to the current axis
ax = plt.gca()
# HERE
ax.set_title('title for this axis only', fontsize=20)
