import yfinance as yf

tkr= yf.Ticker('TSLA')
hist = tkr.history(period="5D")
hist = hist.drop("Dividends", axis = 1)
hist = hist.drop("Stock Splits", axis= 1)
hist = hist.reset_index()
hist = hist.set_index('Date')
print(hist)

