# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
# passing 2,2 as parameters indicates that you will
# get 4 subplots (2 rows and 2 columns)
fig, axes = plt.subplots(2,2)
# just plot things on each individual axes
axes[0][0].scatter(x,y,c='red',marker='+')
axes[0][1].bar(x,y)
axes[1][0].scatter(x,y,marker='x')
axes[1][1].barh(x,y)
# you can set the title for a single subplot
axes[1][1].set_title('Plot 4',size=14)
plt.show()

