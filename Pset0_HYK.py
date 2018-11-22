# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:13:22 2018

@author: heyon
"""

''' Problem Set #0
ask the user to enter a number X
ask the user to enter a number Y
prints out the number X raised to the power of Y
prints out the log 2 of X'''

import math 
import numpy as np

a = input("Enter a number for X:")
b = input("Enter a number for Y:")

print("") # just to make some separation
print('X to the power of Y:', int(a)**int(b))
print("")
# print(int(math.floor(math.log(int(a),2))))
# print("log 2 of X:", math.log(int(a),2))
print('log 2 of X:', np.log2(int(a)))

# my keyboard does not have a backslash so how do I start a new line?