import ta

def add_indicators(df):
    df["SMA_20"] = ta.trend.sma_indicator(df["Close"], 20)
    df["SMA_50"] = ta.trend.sma_indicator(df["Close"], 50)
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)
    return df
