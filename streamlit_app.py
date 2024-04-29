import streamlit as st 
import numpy  as np
import pandas as pd
import json
from streamlit.web.server.websocket_headers import _get_websocket_headers

websocket_headers = _get_websocket_headers()
kbc_user_email = websocket_headers.get('X-Kbc-User-Email', '')
app_trace_id = websocket_headers.get('X-Appgw-Trace-Id', '')
original_host = websocket_headers.get('X-Original-Host', '')

# Set the app title 
st.title('Test editace metadat') 
have_it = None
cnt = 1

st.write(kbc_user_email) 
st.write(original_host)

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
        cnt = cnt + 1
        st.write(cnt) 
        have_it = False
    else:
        st.write('Nestisknuto')
        cnt = cnt + 1
        st.write(cnt)
        have_it = True


# Add a welcome message 
#st.write('Welcome to my Streamlit app!') 
# Create a text input 
#widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
#st.write('Customized Message:', widgetuser_input)
