# Import necessary packages (* Make sure to also include in "requirements.txt" in this repository
import streamlit as st
import yfinance as yf
import pandas as pd

# Print Title for the App
st.title("Tabs version of code")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for ")
    
# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for ")
    
# Tab 3: Volume Chart
with tabs[2]:
     st.subheader(f"Volume for ")
