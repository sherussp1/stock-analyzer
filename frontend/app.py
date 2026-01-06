import streamlit as st
import requests

st.title("📈 AI Stock Analyzer")

symbol = st.text_input("Stock Symbol", "AAPL")
model = st.selectbox("Prediction Model", ["prophet", "lstm"])

if st.button("Analyze"):
    res = requests.get(f"http://localhost:8000/analyze/{symbol}?model={model}")
    data = res.json()

    st.metric("Signal", data["signal"])
    st.metric("Predicted Price", data["prediction"])
    st.metric("Current Price", data["close_price"])
    st.metric("RSI", data["rsi"])
