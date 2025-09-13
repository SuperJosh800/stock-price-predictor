import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

tickers = ['SPY', 'BIRD','GLD','VTI', 'QQQ'] # SPDR S&P 500 ETF (SPY), Allbirds, Inc. (BIRD), SPDR Gold Shares (GLD), Vanguard Total Stock Market Index Fund ETF Shares (VTI), Invesco QQQ Trust (QQQ)

end_date = datetime.today()
print(end_date)

start_date = end_date - timedelta(days = 2*365)
print(start_date)

close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    close_df[ticker] = data['Close']

    print(close_df)