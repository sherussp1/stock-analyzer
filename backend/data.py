import yfinance as yf

def fetch_stock_data(symbol: str, period="1y"):
    return yf.Ticker(symbol).history(period=period)
