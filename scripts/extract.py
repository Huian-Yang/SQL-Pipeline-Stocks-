import yfinance as yf
import pandas as pd
import os

# A few stocks from my own portfolio 

# Ratheon Technologies Corporation (RTX)
# Celestica (CLS)
# Veritex Holdings (VRT)
# Credo Technology Group (CRDO)
# ESCO Technologies (ESE)
# Figma (FIG)
# Ouster (OUST)
tickers = ['RTX', 'CLS', 'VRT', 'CRDO', 'ESE', 'FIG', 'OUST']

all_data = []

for ticker in tickers:
    df = yf.download(ticker, period = "1y", interval = "1d")
    df["ticker"] = ticker
    df = df.reset_index() # Reset index to make 'Date' a column
    all_data.append(df)

prices = pd.concat(all_data, ignore_index=True)

# os.makedirs("data/raw")
prices.to_csv("data/raw/stock_prices.csv", index=False)


