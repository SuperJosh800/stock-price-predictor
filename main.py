import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import sleep

def stocks_download():
    tickers = ['SPY', 'BIRD','GLD','VTI', 'QQQ'] # SPDR S&P 500 ETF (SPY), Allbirds, Inc. (BIRD), SPDR Gold Shares (GLD), Vanguard Total Stock Market Index Fund ETF Shares (VTI), Invesco QQQ Trust (QQQ)

    end_date = datetime.today()
    print(end_date)

    start_date = end_date - timedelta(days = 2*365) # how many years of data we download
    print(start_date)

    data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')

    all_data = []

    for ticker in tickers:
        df = data[ticker].copy() #gets the tickers data
        df.reset_index(inplace=True)  #moves date out of index and into own colum
        df['Ticker'] = ticker         #makes column to remember ticker
        all_data.append(df)           # stores it for later

    df2 = pd.concat(all_data)

    df2 = df2[['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']] # colums
    main_df = df2.dropna #removes empty cells from df

    df2.to_csv('stocks.csv', index=False)

    

def stocks_plot():
    
    df = pd.read_csv('stocks.csv')

    df.plot()

    plt.show()

# this isnt working right (https://www.w3schools.com/python/matplotlib_markers.asp) more here will look into more.

def main():
    
    stocks_download()
    sleep(1)
    stocks_plot()



if __name__ == "__main__":
    main()
    