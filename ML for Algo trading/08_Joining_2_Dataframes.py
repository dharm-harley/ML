# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:34:04 2019

@author: M0078529
"""


import pandas as pd

def test_run():
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)
    print(dates)    #printing entire range of elements 
    print(dates[0]) #printing 1st Element 
    
    df1=pd.DataFrame(index=dates)
    print(df1)
    
    #dfSPY=pd.read_csv('data/spy.csv')
    #print(dfSPY)
    
    #df1=df1.join(dfSPY) #joining 2 dataframes without matching index
    #print(df1)
    
    #dfSPY=pd.read_csv('data/spy.csv',index_col="Date",parse_dates=True)
    #print(dfSPY)
    
    dfSPY=pd.read_csv('data/spy.csv',
                      index_col="Date",
                      parse_dates=True,
                      usecols=['Date','Adj Close'],na_values=['nan']) #na_values['nan'] converts str to NaN
    
    df1=df1.join(dfSPY) #joining 2 dataframes with matching index ie dates
    print(df1)
    
    df1=df1.dropna()
    print(df1)
    
if __name__=="__main__":
    test_run()