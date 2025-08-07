import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime

# --- カスタムCSSで全体デザインを調整 ---
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #e0e7ff 0%, #f0fdfa 100%);
        font-family: 'Segoe UI', 'Meiryo', sans-serif;
    }
    .main .block-container {
        background: rgba(255,255,255,0.95);
        border-radius: 18px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.08);
        padding: 2rem 2.5rem;
        margin-top: 2rem;
    }
    .sidebar .sidebar-content {
        background: #312e81;
        color: #fff;
        border-radius: 16px;
        padding: 1.5rem 1rem;
    }
    .sidebar .sidebar-content h2, .sidebar .sidebar-content h3, .sidebar .sidebar-content h4 {
        color: #a5b4fc;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #06b6d4 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: bold;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #06b6d4 0%, #6366f1 100%);
        color: #fff;
    }
    .stDataFrame, .stTable {
        background: #f1f5f9;
        border-radius: 10px;
        padding: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- サイドバー ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/2/20/Yahoo%21_Japan_logo_2013.svg", width=180)
st.sidebar.markdown("""
### Yahoo!ファイナンス ダッシュボード
銘柄の株価を手軽にチェック！
""")
st.sidebar.header("設定")
ticker = st.sidebar.text_input("銘柄コード（例: AAPL, MSFT, 7203.T）", "AAPL")
period = st.sidebar.selectbox("期間", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "max"], index=5)
interval = st.sidebar.selectbox("間隔", ["1m", "5m", "15m", "1h", "1d", "1wk", "1mo"], index=4)

# --- メインエリア ---
st.markdown("""
<div style='display: flex; align-items: center; gap: 1rem;'>
    <span style='font-size:2.5rem;'>📈</span>
    <h1 style='margin-bottom:0;'>Yahoo!ファイナンス ダッシュボード</h1>
</div>
<hr style='border: 1px solid #6366f1; margin-top: 0.5rem; margin-bottom: 2rem;'>
""", unsafe_allow_html=True)

if st.sidebar.button("データ取得"):
    with st.spinner("データ取得中..."):
        data = yf.download(ticker, period=period, interval=interval)
    if not data.empty:
        st.markdown(f"<div style='background: #f1f5f9; border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; box-shadow: 0 2px 8px rgba(99,102,241,0.08);'>"
                    f"<h3 style='color:#312e81;'>🗂 {ticker} の株価終値チャート</h3>", unsafe_allow_html=True)
        st.line_chart(data["Close"])
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background: #f1f5f9; border-radius: 12px; padding: 1.5rem; margin-bottom: 2rem; box-shadow: 0 2px 8px rgba(99,102,241,0.08);'>"
                    f"<h3 style='color:#312e81;'>📋 データテーブル</h3>", unsafe_allow_html=True)
        st.dataframe(data)
        st.markdown("</div>", unsafe_allow_html=True)
        st.success(f"データ取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.warning("データが取得できませんでした。銘柄コードや期間を確認してください。") 