import numpy as np
import yfinance as yf
import pandas as pd

# Importation of data
list_tickers = ["AAPL"]
data = yf.download(list_tickers)

# For tick calculation(The smallest unit of change)
for i in range(0, len(data)):
    data['tick'] = data['Close'] - data['Open']

print(data)

