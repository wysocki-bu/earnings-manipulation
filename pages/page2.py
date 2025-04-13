import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Page 2: Financials")

aapl = yf.Ticker("AAPL")
balance_sheet = aapl.balance_sheet
#print(balance_sheet)
st.write(balance_sheet)

st.write(balance_sheet.iloc[[40,51,61],])


#if 'data' in st.session_state:
#   st.write("Statistics of the DataFrame:")
#   st.write(st.session_state.data.describe())
#else:
#   st.write("No stock data found. Please select stock on Main Page.")
