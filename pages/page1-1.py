import streamlit as st

st.title("1) Original Code for Training Abnormal Accruals Model")

st.write("The Colab Notebook can be found here: https://colab.research.google.com/drive/16ipr04946UfsPOJaROpUxUt-1L6pF-jW?usp=sharing")

# The original Colab Notebook Python Code can be found here:
# https://colab.research.google.com/drive/16ipr04946UfsPOJaROpUxUt-1L6pF-jW?usp=sharing

with open('pages/model1.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
