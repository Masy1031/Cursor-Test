import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Yahooファイナンス ダッシュボード")

# ユーザー入力
st.sidebar.header("設定")
ticker = st.sidebar.text_input("銘柄コード（例: AAPL, MSFT, 7203.T）", "AAPL")
period = st.sidebar.selectbox("期間", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "max"], index=5)
interval = st.sidebar.selectbox("間隔", ["1m", "5m", "15m", "1h", "1d", "1wk", "1mo"], index=4)

if st.sidebar.button("データ取得"):
    data = yf.download(ticker, period=period, interval=interval)
    if not data.empty:
        st.subheader(f"{ticker} の株価終値チャート")
        st.line_chart(data["Close"])
        st.subheader("データテーブル")
        st.dataframe(data)
    else:
        st.warning("データが取得できませんでした。銘柄コードや期間を確認してください。") 