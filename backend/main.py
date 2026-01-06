from fastapi import FastAPI
from backend.data import fetch_stock_data
from backend.indicators import add_indicators
from backend.signals import generate_signal
from backend.ml_prophet import predict_price_prophet
from backend.ml_lstm import predict_price_lstm

app = FastAPI()

@app.get("/analyze/{symbol}")
def analyze(symbol: str, model: str = "prophet"):
    df = fetch_stock_data(symbol)
    df = add_indicators(df)

    signal = generate_signal(df)

    if model == "lstm":
        prediction = predict_price_lstm(df)
    else:
        prediction = predict_price_prophet(df)

    return {
        "symbol": symbol,
        "signal": signal,
        "prediction": round(prediction, 2),
        "close_price": round(df["Close"].iloc[-1], 2),
        "rsi": round(df["RSI"].iloc[-1], 2)
    }
