# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:19:46 2019

@author: M0078529
"""


import os
import pandas as pd 
import matplotlib.pyplot as plt

def plot_selected(df,columns,start_index,end_index):
    
    plot_data(df.ix[start_index:end_index,columns],title="selected data")    

def symbol_to_path(symbol, base_dir = 'data'):
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	df = pd.DataFrame(index = dates)
	if 'SPY' not in symbols: # adding SPY as the main reference
		symbols.insert(0, 'SPY')
	for symbol in symbols:
		df_temp = pd.read_csv(symbol_to_path(symbol),
			index_col = 'Date',
			parse_dates = True,
			usecols = ['Date', 'Adj Close'],
			na_values = ['nan'])
		df_temp = df_temp.rename(columns = {'Adj Close': symbol})
		df = df.join(df_temp)
	
		if symbol == 'SPY':
			df = df.dropna(subset = ['SPY'])

	#print(df)
	return df
     
def plot_data(df,title='Stock Prices'):
    ax=df.plot(title=title,fontsize=2)
    ax.set_xlabel('Date')
    ax.set_ylabel('price')
    plt.show()
    

def test_run():
    #defining date range
    dates=pd.date_range('2010-01-01','2010-12-31')
    
    #Choosing symbols
    symbols=['GOOG','IBM','GLD'] #SPY will be added in get_data()
    
    #Get stock data
    df=get_data(symbols,dates)
    
    #Slice and plat
    plot_selected(df,['SPY','IBM'],'2010-03-01','2010-04-01')

if __name__=="__main__":
    test_run()