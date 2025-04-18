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

   balance_sheet.columns = range(len(balance_sheet.columns))
   st.write(balance_sheet.loc[['Total Assets'],1])
   st.write(balance_sheet.loc[['Gross PPE'],0])


# Tab 3: Forecast Abnormal Accruals
with tabs[2]:

   # load model
   # Display the results in Streamlit
   st.title("Parameters of Trained OLS Model")

   # Display the model summary
   st.write("Model Summary:")
   st.write(loaded_model.summary())

   #create new DataFrame
   df_new = pd.DataFrame({'hours': [1, 2, 2, 4, 5],
                       'exams': [1, 1, 4, 3, 3]})

   #add column for constant
   df_new = sm.add_constant(df_new)

   #view new DataFrame
   #print(df_new)

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
