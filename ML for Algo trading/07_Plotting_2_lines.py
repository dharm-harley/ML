# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:29:02 2019

@author: M0078529
"""

import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df=pd.read_csv("data/AAPL.csv") #reading Apple Adj Close Prices
    df[['Adj Close','Close']].plot() #plotting 2 lines
    plt.show()


test_run()