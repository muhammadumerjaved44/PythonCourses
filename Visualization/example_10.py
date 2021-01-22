# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# generate sample data for this example
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
# HERE linewidth and linestyle are some of the options you can set
# gca means Get Current Axis
plt.gca().grid(True, linewidth=0.7, linestyle=':')
# then plot the chart as you would normally
plt.plot(x,y)
