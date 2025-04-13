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
        st.session_state['df'] = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})

        
#        st.session_state['df'] = pd.DataFrame(
#            [
#              {"command": "st.selectbox", "rating": 4, "is_widget": True},
#              {"command": "st.balloons", "rating": 5, "is_widget": False},
#              {"command": "st.time_input", "rating": 3, "is_widget": True},
#            ]
#        ) 
     edited_df = st.data_editor(st.session_state['df'])
     st.session_state['df'] = edited_df    
      
# Tab 2: Get Data from YFinance
with tabs[1]:
    st.subheader("Look Up Data in Real Time - Ticker")

# Tab 3: Blank
with tabs[2]:
    st.subheader("Blank for the moment")
