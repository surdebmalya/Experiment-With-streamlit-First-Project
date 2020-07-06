import yfinance as yf
import streamlit as st

st.title("""
Stock Pricing App On Google Historical Dataset
	""")

st.write("""
It is my first Experiment on ***streamlit***. Here I deploy a easy visulization system. Which is based on Google Dataset.
	""")

st.write("""
Shown are the stock **closing price** and ***volume*** of Google!
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)