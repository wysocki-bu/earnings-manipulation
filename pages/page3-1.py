# Import necessary packages (* Make sure to also include in "requirements.txt" in this repository
import streamlit as st
import pandas as pd
import yfinance as yf

st.title("2) Forecast Using Trained Model")
st.header("   Select Tab in Sequence to Forecast Abnormal Accruals for a Stock Ticker")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Select Ticker", "📈 View Forecasted Accruals", "📊 Change Ratios (What If?)"])

# Tab 1: Select Ticker 
with tabs[0]:
   ticker_symbol = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
   tic = yf.Ticker(ticker_symbol)

   balance_sheet = tic.balance_sheet
   if balance_sheet.empty:
      st.error("No data found. Please check the ticker symbol.")
      st.stop()
   st.write(balance_sheet.loc[['Total Assets','Gross PPE','Accounts Receivable'],:])

   income_statement = tic.income_stmt
   st.write(income_statement.loc[['Total Revenue'],:])

   cash_flow = tic.cashflow
   st.write(cash_flow.loc[['Operating Cash Flow','Net Income From Continuing Operations'],:])

   
   
   
   st.subheader("Code for Page 1")
   with open('pages/page1.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
    
# Tab 2: page2.py
with tabs[1]:
   st.subheader(f"Code for Page 2")
   with open('pages/page2.py', 'r') as file:
      code = file.read()
      st.code(code, language='python')

# Tab 3: page3.py
with tabs[2]:
    st.subheader(f"Code for Page 3")
    with open('pages/page3.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')

st.divider() 

st.subheader("Streamlit Python Code for this page:")
with open('pages/page3-1.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
