import streamlit as st 
import numpy  as np
import pandas as pd
import json
from streamlit.web.server.websocket_headers import _get_websocket_headers

websocket_headers = _get_websocket_headers()
kbc_user_email = websocket_headers.get('X-Kbc-User-Email', '')
app_trace_id = websocket_headers.get('X-Appgw-Trace-Id', '')
original_host = websocket_headers.get('X-Original-Host', '')
host =  websocket_headers.get('Host', '')

# Set the app title 
st.title('Test editace metadat') 
have_it = None
cnt = 1

st.write(host) 

menu = ["Home","About"]
choice = st.sidebar.selectbox("Menu",menu)
if choice == "Home":
    st.subheader("HomePage")
else:
    st.subheader("About")

input_df = pd.DataFrame.from_dict(
#{   
#    'Jméno': ["Filip", "Martin"],
#    'Příjmení': ["Ruka", "Noha"],
#    'Score': [1555, 222],
#}
{"OKOPROD_SOURCE_ID":{"0":"PENSION_INC"},"OKOPROD_NAME":{"0":"Nav\u00fd\u0161en\u00ed penze"},"OKOPROD_NAME_ENG":{"0":"Pension Insurance - upsale"},"OKOPROD_PARENT_ID":{"0":"XSPEC_D"},"OKOPROD_HIER_LEVEL":{"0":3},"OKOPROD_LEAF_FLAG":{"0":"Y"},"OKOPROD_VALID_FROM":{"0":1577836800000},"OKOPROD_VALID_TO":{"0":32503680000},"OKOPROD_INSERTED_DATETIME":{"0":1637245931000},"OKOPROD_UPDATED_DATETIME":{"0":1637245931000},"INSERT_PROCESS_KEY":{"0":12028621},"INSERT_TASKINS_KEY":{"0":143928354},"_timestamp":{"0":1714626194000}}
,orient='columns')


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
