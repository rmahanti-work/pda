#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:36:34 2020

@author: kanthi
"""
import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
print(x)

y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(y)

print(x.dot(y))

print(np.ones(3))
print(np.dot(x, np.ones(3)))