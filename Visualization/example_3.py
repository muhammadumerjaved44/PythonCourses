# -*- coding: utf-8 -*-
Save plot to file
The image format is deduced from the extension (’png’, ’jpg’, ’svg’, etc)
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)
plt.scatter(x,y)
plt.savefig('out.png')

