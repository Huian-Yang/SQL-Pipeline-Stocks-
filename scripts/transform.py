import pandas as pd

df = pd.read_csv("../data/raw/stock_prices.csv")
df.columns = [col.lower().replace(" ", "_") for col in df.columns]
df['date'] = pd.to_datetime(df['date'])
df = df.drop_duplicates()
df = df.sort_values(by=['ticker', 'date'])
df = df.dropna() #Drop NA values

df["daily_return"] = df.groupby("ticker")["close"].pct_change()
df["ma_7"] = df.groupby("ticker")["close"].transform(lambda x: x.rolling(window=7).mean()) # moving average (week)
df["ma_30"] = df.groupby("ticker")["close"].transform(lambda x: x.rolling(window=30).mean()) # moving average (month)

df.to_csv("../data/cleaned/clean_stock_prices.csv", index=False)
 






print(df.head())
