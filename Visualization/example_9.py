# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
# for the whole plot
plt.plot(x,y)
# HERE
plt.ylim(-5,15)
plt.xlim(-30,130)

