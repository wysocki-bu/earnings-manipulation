import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Page 2: Financials")

ticker_symbol = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")

#aapl = yf.Ticker("AAPL")
tic = yf.Ticker(ticker_symbol)

balance_sheet = tic.balance_sheet
#st.write(balance_sheet)
st.write(balance_sheet.iloc[[40,51,62],])

income_statement = tic.income_stmt
#st.write(income_statement)
st.write(income_statement.iloc[[23],])

cash_flow = tic.cashflow
#st.write(cash_flow)
st.write(cash_flow.iloc[[34,35,45,52],])


#if 'data' in st.session_state:
#   st.write("Statistics of the DataFrame:")
#   st.write(st.session_state.data.describe())
#else:
#   st.write("No stock data found. Please select stock on Main Page.")
