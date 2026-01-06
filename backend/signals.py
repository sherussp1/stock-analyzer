def generate_signal(df):
    if df["SMA_20"].iloc[-1] > df["SMA_50"].iloc[-1] and df["RSI"].iloc[-1] < 70:
        return "BUY"
    elif df["SMA_20"].iloc[-1] < df["SMA_50"].iloc[-1] and df["RSI"].iloc[-1] > 30:
        return "SELL"
    return "HOLD"
