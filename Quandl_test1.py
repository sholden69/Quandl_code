import quandl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Read my quandl API key
quandl.read_key("../.quandl_apikey")
print(quandl.ApiConfig.api_key)

#input data
bank_tickers=['MS','GS','JPM','BAC']

# API call to list all the tickers in the WIKI dataset - looks like it might be deprecated
# https://www.quandl.com/api/v3/databases/WIKI/metadata?api_key=TkzGdrC6nswPnuxzfzPZ

#data1 = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2020-01-10", ticker=['MS'],authtoken="TkzGdrC6nswPnuxzfzPZ")
#print(data1)

print("------------------------------------------------------------------")
# Source MS, GS, BAC stock prices for the last 20 years
data2 = quandl.get_table('WIKI/PRICES', ticker = bank_tickers,
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] },
                        date = { 'gte': '2000-01-01', 'lte': '2022-01-11' },
                        paginate=True)
#print(data2)

# create a new dataframe with 'date' column as index
new = data2.set_index('date')

# use pandas pivot function to sort adj_close by tickers
clean_data = new.pivot(columns='ticker')
clean_data.info()


# check the head of the output
print(clean_data)
plt.plot(clean_data)
plt.legend(bank_tickers,loc='upper left')
plt.title('US Bank Stocks 2000-2022')
plt.show()
