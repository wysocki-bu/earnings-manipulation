# Import necessary packages (* Make sure to also include in "requirements.txt" in this repository
import streamlit as st
import yfinance as yf
import pandas as pd

# Print Title for the App
st.title("5. Tabs version of app code")

# Set up the 3 tabs on the Dashboard
tabs = st.tabs(["📋 page1.py", "📈 page2.py", "📊 page3.py"])

# Tab 1: page1.py 
with tabs[0]:
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
