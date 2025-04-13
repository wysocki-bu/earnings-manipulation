import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Page 2: Financials")

aapl = yf.Ticker("AAPL")
balance_sheet = aapl.balance_sheet
#st.write(balance_sheet)
st.write(balance_sheet.iloc[[40,51,62],])

income_statement = aapl.income_stmt
#st.write(income_statement)
st.write(income_statement.iloc[[23],])

cash_flow = aapl.cashflow
#st.write(cash_flow)
st.write(cash_flow.iloc[[34,35,45],])


#if 'data' in st.session_state:
#   st.write("Statistics of the DataFrame:")
#   st.write(st.session_state.data.describe())
#else:
#   st.write("No stock data found. Please select stock on Main Page.")
