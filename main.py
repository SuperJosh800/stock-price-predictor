import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta


tickers = ['SPY', 'BIRD','GLD','VTI', 'QQQ'] # SPDR S&P 500 ETF (SPY), Allbirds, Inc. (BIRD), SPDR Gold Shares (GLD), Vanguard Total Stock Market Index Fund ETF Shares (VTI), Invesco QQQ Trust (QQQ)

end_date = datetime.today()
print(end_date)

start_date = end_date - timedelta(days = 5*365)
print(start_date)

data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')

all_data = []

for ticker in tickers:
    df = data[ticker].copy() #gets the tickers data
    df.reset_index(inplace=True)  #moves date out of index and into own colum
    df['Ticker'] = ticker         #makes column to remember ticker
    all_data.append(df)           # stores it for later

final_df = pd.concat(all_data)

final_df = final_df[['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']] # colums

final_df.to_csv('stocks.csv', index=False)