import streamlit as st 
import numpy  as np
import pandas as pd
import json
#from kbcstorage.client import Client
# Set the app title 
st.title('My First Streamlit Appka') 
# Add a welcome message 
st.write('Welcome to my Streamlit app!') 
# Create a text input 
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
st.write('Customized Message:', widgetuser_input)
