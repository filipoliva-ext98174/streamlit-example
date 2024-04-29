import streamlit as st 
import numpy  as np
import pandas as pd
import json

# Set the app title 
st.title('My First Streamlit Appka') 
menu = ["Home","About"]
choice = st.sidebar.selectbox("Menu",menu)
if choice == "Home":
    st.subheader("HomePage")
else:
    st.subheader("About")

input_df = pd.DataFrame.from_dict({
    'field_1': ["some", "values"],
    'field_2': ["other", "values"],
    'field_3': range(1, 2)
})
st.write(input_df)

# Add a welcome message 
#st.write('Welcome to my Streamlit app!') 
# Create a text input 
#widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
#st.write('Customized Message:', widgetuser_input)
