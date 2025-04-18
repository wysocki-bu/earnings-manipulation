import streamlit as st

st.title("5. Code for this StreamLit App")
st.subheader("Note that there are code blocks for each page in this app.")
st.subheader("The blocks are listed separately below.")


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

st.subheader("Code for Page 3")
with open('pages/page3.py', 'r') as file:
            code = file.read()
            st.code(code, language='python')
