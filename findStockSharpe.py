def findStockSharpe(fileName):
	import numpy as np
	import pandas as pd
	import matplotlib as plt
	import matplotlib.dates as date
	import datetime
	%matplotlib inline
	from numpy.random import randn

	stock = pd.read_csv(fileName, parse_dates=['Date'], dayfirst =True)
	stock= stock.drop(stock.columns[[1,2,3,4,6]], axis=1)
	stock=stock.set_index(stock.columns[0])
	stock_returns = stock.pct_change()
	stock_mean_return = stock_returns.mean()
	stock_return_stdev = stock_returns.std()
	stock_annualised_return = round(stock_mean_return * 252,2)
	stock_annualised_stdev = round(stock_return_stdev * np.sqrt(252),2)
	stock_sharpe_ratio=(stock_mean_return/stock_return_stdev)
	stock_sharpe_ratio=(252**0.5)*stock_sharpe_ratio

	print("The annualised mean return of stock is {}".format(stock_annualised_return.values))
	print("The annualised volatility is {}".format(stock_annualised_stdev.values))
	print("Sharpe Ratio of stock is {}".format(stock_sharpe_ratio.values))
