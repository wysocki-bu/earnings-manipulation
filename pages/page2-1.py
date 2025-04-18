import streamlit as st
import statsmodels.api as sm
import pickle

filename = 'pages/ols_model.pkl'

# Load the model
loaded_model = pickle.load(open(filename, 'rb'))

# Display the results in Streamlit
st.title("2) Parameters of Trained OLS Model")

# Display the model summary
st.write("Model Summary:")
st.write(loaded_model.summary())
