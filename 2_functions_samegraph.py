#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: haimagull
How to plot on the same axis two simple functions using Matplotlib et Scipy ? Example : ln(2n) and ln(n^2)
"""
#import libraries
import matplotlib.pyplot as plt
import numpy as np

#define variables
n = np.linspace(1,5000) #pre made functions can create linear/scattered space
ln2n = np.log(2*n) #applying the function
lnn2 = np.log(n**2)


"""plot : OO type ('Object oriented')"""
fig, ax1 = plt.subplots()
ax1.set_xlabel(r'$n$') #x label (r string is necessary to use latex)
ax1.set_ylabel([r'$log(2n)$',r"$ln(n^2)$"]) #y label (idem)
ax1.set_title(r'Évolution du logarithme en base 10 pour une varible doublée') #title
ax1.plot(n,ln2n,"b") #actually plotting the first one
ax1.plot(n,lnn2,"red") #actually plotting the second one
"""figure settings"""
fig.set_size_inches(7,5) #graph dimensions
fig.set_dpi(200) #resolution (dot per inches)
fig.legend([r"$ln(2n)$",r"$ln(n^2)$"]) #a legend might be interesting if plotting multiple functions
plt.show() #let's see what we just did :)
