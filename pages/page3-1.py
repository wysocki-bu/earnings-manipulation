import streamlit as st
import pandas as pd
import yfinance as yf

st.title("2) Financials")

ticker_symbol = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")

#aapl = yf.Ticker("AAPL")
tic = yf.Ticker(ticker_symbol)

balance_sheet = tic.balance_sheet
if balance_sheet.empty:
   st.error("No data found. Please check the ticker symbol.")
   st.stop()
#st.write(balance_sheet)
st.write(balance_sheet.loc[['Total Assets','Gross PPE','Accounts Receivable'],:])

income_statement = tic.income_stmt
#st.write(income_statement)
st.write(income_statement.loc[['Total Revenue'],:])

cash_flow = tic.cashflow
#st.write(cash_flow)
st.write(cash_flow.loc[['Operating Cash Flow','Net Income From Continuing Operations'],:])

st.divider() 

st.subheader("Streamlit Python Code for this page:")
with open('pages/page2.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')

#if 'data' in st.session_state:
#   st.write("Statistics of the DataFrame:")
#   st.write(st.session_state.data.describe())
#else:
#   st.write("No stock data found. Please select stock on Main Page.")
