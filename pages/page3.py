import streamlit as st

st.title("Page 3: Original Code for Training Abnormal Accruals Model")

# The original Colab Notebook Python Code can be found here:
# http:

code = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm'''

st.code(code, language="python")


#st.title("Page 3: Close Price data")

# Plot a Linbe Chart of the Stock Price of the stock
#if 'data' in st.session_state:
#   st.line_chart(st.session_state.data['Close'])

#else:
#   st.write("No stock data found. Please select stock on Main Page.")
