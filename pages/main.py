import streamlit as st
import pandas as pd
import yfinance as yf

# Print out info for the Main page:
st.title("Find Abnormal Accruals for a Stock")
st.header("Modified Jones Model App")
st.subheader("What, How, Why?")

st.markdown(''' :rainbow[What?]''')
st.write("This App trains a version of <Modified Jones Model> using data from Compustat to determine the")
st.write("regular association between operations and accruals. Abnormal accruals are the residuals (e)")
st.write("from the model below:")
 
st.image("pages/files/jonesmodel.png", caption="The model of normal accruals: The Modified Jones Model")

st.write(f"Wh: .")
st.write(f"How: .")

url = "https://github.com/wysocki-bu/earnings-manipulation/"
st.write("Link to GitHub respository for StreamLit App is here:")
st.write("[https://github.com/wysocki-bu/earnings-manipulation/](%s)" %url)




# Sidebar inputs for ticker symbol and dates
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-12-31"))

# Print update onb which ticker and dates
st.write(f"You have selected **{ticker_symbol}** from {start_date} to {end_date}.")
st.markdown(''':red[Now click on] :blue-background[selections 1-5] to the left to view analyses.''')

# Access the stock data for the given tocker using the yfinance "download" function
# Temporarily store data in "df" dataframe
df = yf.download(ticker_symbol, start=start_date, end=end_date)
if df.empty:
   st.error("No data found. Please check the ticker symbol or date range.")
   st.stop()


#  Note: The stock info dataframe (df) is stored in a StreamLit "session state" that allows the data to be shared across
#        the mutiple pages (ie, main.py, page1.py, page2.py and page4.py)
st.session_state.data = df
