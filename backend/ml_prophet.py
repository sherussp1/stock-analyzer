from prophet import Prophet

def predict_price_prophet(df):
    data = df.reset_index()[["Date", "Close"]]
    data.columns = ["ds", "y"]

    # 🔧 FIX: remove timezone (CRITICAL)
    data["ds"] = data["ds"].dt.tz_localize(None)

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=5)
    forecast = model.predict(future)

    return float(forecast["yhat"].iloc[-1])
