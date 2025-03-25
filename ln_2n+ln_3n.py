#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: haimagull
How to plot at the same time two simple graphs using Matplotlib et Scipy ? Example : ln(2n) and ln(n^2)

"""
#import libraries
import matplotlib.pyplot as plt
import numpy as np

#define variables
n = np.linspace(1,5000) #pre made functions can create linear/scattered space
ln2n = np.log(2*n) #applying the function
lnn2 = np.log(n**2)

"""plot : OO ('Object oriented')"""
#first function
fig, ax1 = plt.subplots()
ax1.set_xlabel(r'$n$') #x label (r string is necessary to use latex)
ax1.set_ylabel(r'$log(2n)$', color="blue") #y label (idem)
ax1.set_title(r'\'Evolution du logarithme en base 10 pour une varible doubl\'ee') #title
ax1.plot(n,ln2n,"b") #actually plotting

fig.set_size_inches(7,5) #graph dimensions
fig.set_dpi(200) #resolution (dot per inches)
fig.legend([r"$ln(2n)$"]) #a legend might be interesting if plotting multiple functions
plt.show() #let's see what we just did !

#second function
fig, ax2 = plt.subplots()
ax2.set_xlabel(r'$n$') #x label (r string is necessary to use latex)
ax2.set_ylabel(r'$log(n^2)$',color="red") #y label (idem)
ax2.set_title(r'\'Evolution du logarithme en base 10 pour une varible au carr\'e) #title
ax2.plot(n,lnn2,"red") #actually plotting


fig.set_size_inches(7,5) #graph dimensions
fig.set_dpi(200) #resolution (dot per inches)
fig.legend([r"$ln(n^2)$"]) #a legend might be interesting if plotting multiple functions
plt.show() #let's see this one two while we're at it
