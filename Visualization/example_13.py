# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# sample data
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
# plt.subplots returns an array of arrays. We can
# directly assign those to variables directly
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
# just plot things on each individual axes
ax1.scatter(x,y,c='red',marker='+')
ax2.bar(x,y)
ax3.scatter(x,y,marker='x')
ax4.barh(x,y)
plt.show()

