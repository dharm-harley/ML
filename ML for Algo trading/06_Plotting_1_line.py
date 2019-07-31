# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:28:21 2019

@author: M0078529
"""

import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df=pd.read_csv("data/AAPL.csv") #reading Apple Adj Close Prices
    df['Adj Close'].plot()
    plt.show()

    df=pd.read_csv("data/IBM.csv")  #reading IBM High -Prices
    df['High'].plot()
    plt.show()


test_run()