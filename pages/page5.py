import streamlit as st

st.title("Page 5: Code for this StreamLit App")

# The original Github repository for this app can be found here:
# http:

st.subheader("Code for Page 1")
with open('pages/page1.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')

st.subheader("Code for Page 2")
with open('pages/page2.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
