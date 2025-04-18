# Import necessary packages (* Make sure to also include in "requirements.txt" in this repository
import streamlit as st
import yfinance as yf
import pandas as pd

# Print Title for the App
st.title("3. Enter Stock Financial Data")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 Manual Data Entry", "📈 Automatic Using Ticker", "📊 Empty"])

# Tab 1: Manual Data Entry 
with tabs[0]:
    st.subheader("Manually Enter Stock Information")
    if 'df' not in st.session_state:
        st.session_state['df'] = pd.DataFrame({'col1': [], 'col2': []})
    edited_df = st.data_editor(st.session_state['df'])
    st.session_state['df'] = edited_df    
      
# Tab 2: Get Data from YFinance
with tabs[1]:
    age = st.slider("How old are you?", 0, 130, 25)
    st.write("I'm ", age, "years old")

# Tab 3: Blank
with tabs[2]:
    st.subheader("Blank for the moment")
    values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
    st.write("Values:", values)
