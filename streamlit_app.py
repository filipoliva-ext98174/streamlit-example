import streamlit as st 
import numpy  as np
import pandas as pd
import json

# Set the app title 
st.title('Test editace metadat') 
#have_it = False
menu = ["Home","About"]
choice = st.sidebar.selectbox("Menu",menu)
if choice == "Home":
    st.subheader("HomePage")
else:
    st.subheader("About")

input_df = pd.DataFrame.from_dict({
    'Jméno': ["Filip", "Martin"],
    'Příjmení': ["Ruka", "Noha"],
    'Score': [1555, 222],
})

#st.write(input_df)
st.experimental_data_editor(input_df)
if st.button('Zjisti jméno'):
    if have_it == True:
        st.write('Stisknuto') 
        st.write(have_it) 
        have_it = False
    else:
        st.write('Nestisknuto')
        st.write(have_it)
        have_it = True


# Add a welcome message 
#st.write('Welcome to my Streamlit app!') 
# Create a text input 
#widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
#st.write('Customized Message:', widgetuser_input)
