#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 14:32:07 2020

@author: kanthi
"""


import numpy as np

''' Handling binary files in Numpy '''
''' single or multiple arrays can be saved to binay files '''
''' single file extension - .npy '''
''' multiple file extension - .npz '''

arr = np.arange(10)

np.save('arr_file', arr)

print(np.load('arr_file.npy'))

a = arr * 10
b = arr * 20

print(a)
print(b)
np.savez('arr_s_file.npy', a=a, b=b)

arch = np.load('arr_s_file.npy.npz')
print(arch['a'])

