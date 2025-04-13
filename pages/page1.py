import streamlit as st
import pandas as pd

# Print out the title for Page 1: View stock info dataframe
st.title("Page 1: Get SIC Code for Ticker")

# Display the Pandas dataframe of the stock data from yfinance
#  Note: The stock info dataframe is stored in a StreamLit "session state" that allows the data to be shared across
#        the mutiple pages (ie, main.py, page1.py, page2.py and page4.py)

ticker_symbol = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")

#Get the CIK of a ticker from the downloaded cik.csv file
#cik.csv is a tab delimited file with all tickers and CIKs

#location of cik.csv
cikDir = 'pages/cik.csv'

#read cik.csv as a pandas DataFrame
ciksDF = pd.read_csv(cikDir, delimiter='\t', header=None)

#set the column with all the tickers as the index
ciksDF = ciksDF.set_index(0)


#function to return CIK of a ticker
def getCIK(ticker):
    #return CIK if it exists
    try:
        return int(ciksDF.loc[ticker.lower(), 1])

    #return None there's no CIK for the ticker
    except:
        return None
CIK = getCIK(ticker_symbol)

st.write(CIK)

CIK_STR = str(CIK).zfill(10)
st.write(CIK_STR)


#st.dataframe(st.session_state.data, use_container_width=True)

# The dataframe can also be displayed as an editable interactive dataframe using the StreamLit data_editor function 
#st.session_state.data = st.data_editor(st.session_state.data)
