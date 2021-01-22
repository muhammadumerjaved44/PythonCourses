# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# generate sample data for this example
xs = [1,2,3,4,5,6,7,8,9,10,11,12]
ys = np.random.normal(loc=3.0,size=12)
labels = ['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']
plt.bar(xs,ys)
# HERE tell pyplot which labels correspond to which x values
plt.xticks(xs,labels)

