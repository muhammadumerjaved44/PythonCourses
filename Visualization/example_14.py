# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
# sample data
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
# plot individual subplots
ax1.bar(x,y)
ax2.bar(x,y)
ax3.scatter(x,y)
ax4.plot(x)
ax4.set_title('This is Plot 4',size=14)
