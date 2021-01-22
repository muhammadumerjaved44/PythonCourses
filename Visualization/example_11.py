# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
# generate sample data following a normal distribution
values = np.random.normal(size=100)
# array([ 0.49671415, -0.1382643 , 0.64768854,...
# see all examples in the API link
plt.hist(values,rwidth=0.9,bins=[-3,-2,-1,0,1,2,3])
