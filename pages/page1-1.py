import streamlit as st

st.title("1) Original Code for Training Abnormal Accruals Model")

st.subheader("1) The Colab Notebook can be found here: https://colab.research.google.com/drive/16ipr04946UfsPOJaROpUxUt-1L6pF-jW?usp=sharing")


# The original Colab Notebook Python Code can be found here:
# https://colab.research.google.com/drive/16ipr04946UfsPOJaROpUxUt-1L6pF-jW?usp=sharing

code = '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm'''




st.code(code, language="python")

with open('pages/model1.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
