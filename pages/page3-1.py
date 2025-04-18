# Import necessary packages (* Make sure to also include in "requirements.txt" in this repository
import streamlit as st
import pandas as pd
import yfinance as yf
import statsmodels.api as sm
import pickle

filename = 'pages/ols_model.pkl'

# Load the model
loaded_model = pickle.load(open(filename, 'rb'))

st.title("2) Forecast Using Trained Model")
st.header("   Select Tab in Sequence to Forecast Abnormal Accruals for a Stock Ticker")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["> Select Ticker", "> View Ratios", "> View Forecasted Accruals", "> Change Ratios (What If?)"])

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

# Tab 2: Financial Ratios for Ticker
with tabs[1]:
   st.subheader("Calculated Features for MSFT")
   inv_ta = 1/4419
   st.write("1/TA(t-1) = ",inv_ta)
   Dsale_ta = (2451-2119)/4419
   st.write("Dsale(t)/TA(t-1) = ",Dsale_ta)
   ppe_ta = 2310/4419
   st.write("GrossPPE(t)/TA(t-1) = ",ppe_ta)
   roa = 881/4419
   st.write("ROA(t) = ",roa)
   cfo_ta = 1185/4419
   st.write(CFO(t)/TA(t-1) = ",cfo_ta)
   tac_ta = roa - cfo_ta
   st.write("Total Accruals = TAC(t)/TA(t-1) = ", tac_ta)


# Tab 3: Forecast Abnormal Accruals
with tabs[2]:

   # load model
   # Display the results in Streamlit
   st.title("Parameters of Trained OLS Model")

# Tab 4: page3.py
with tabs[3]:
    st.subheader(f"Code for Page 3")
    with open('pages/page3.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')

st.divider() 

st.subheader("Streamlit Python Code for this page:")
with open('pages/page3-1.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
