# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:08:13 2019

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

    dfSPY=pd.read_csv('data/spy.csv',
                      index_col="Date",
                      parse_dates=True,
                      usecols=['Date','Adj Close']) #na_values['nan'] converts str to NaN
    
    dfSPY=dfSPY.rename(columns={'Adj Close':'SPY'}) #Renaming col Adj Close to SPY
     
    df1=df1.join(dfSPY,how='inner') #joining 2 dataframes with matching index ie dates
    print(df1)
    
    symbols=['GOOG','IBM','GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("data/{}.csv".format(symbol), index_col="Date",
                      parse_dates=True,
                      usecols=['Date','Adj Close'])
        df_temp=df_temp.rename(columns={'Adj Close':symbol}) #Renaming to prevent clash of names
        df1=df1.join(df_temp)
    print(df1)
if __name__=="__main__":
    test_run()