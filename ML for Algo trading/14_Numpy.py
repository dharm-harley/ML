# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:06:01 2019

@author: M0078529
"""

import numpy as np 
def create_1D_array():
	array = np.array([2, 3, 4])
	print(array)

def create_2D_array():
	array = np.array([(2, 3, 4),(5, 6, 7)])
	print(array)

if __name__ == "__main__":
	create_1D_array()
	create_2D_array()
	
