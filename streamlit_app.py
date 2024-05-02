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
{"OKOPROD_SOURCE_ID":{"0":"PENSION_INC","1":"XZ_INVESTOR","2":"OTHERA","3":"SA_CA_VNS","4":"XM_LOANSEC_DISC","5":"ERR_OKO","6":"INS_LIFE","7":"PENSION_CONSERV","8":"INV_REGULAR","9":"INV_OTHER"},"OKOPROD_NAME":{"0":"Nav\u00fd\u0161en\u00ed penze","1":"Nov\u00fd investor","2":"Ostatn\u00ed aktiva (souhrn)","3":"Firemn\u00ed spo\u0159\u00edc\u00ed \u00fa\u010det po neziskovky","4":"Z\u00e1kladna slev pro Hypot\u00e9ky","5":"Produkt nedohled\u00e1n v OKO","6":"\u017divotn\u00ed poji\u0161t\u011bn\u00ed","7":"Konzervativn\u00ed Fond","8":"Investice pravideln\u00e9","9":"Ostatn\u00ed cenn\u00e9 pap\u00edry"},"OKOPROD_NAME_ENG":{"0":"Pension Insurance - upsale","1":"New Investor","2":"","3":"","4":"","5":"","6":"Life Insurance","7":"","8":"Investment Regular","9":"Other Securities"},"OKOPROD_PARENT_ID":{"0":"XSPEC_D","1":"XSPEC_Z","2":"ASSETS","3":"SA_CA","4":"XSPEC_M","5":"","6":"INSURANCE","7":"PENSION_3P","8":"XSPEC_D","9":"INVEST"},"OKOPROD_HIER_LEVEL":{"0":3,"1":3,"2":3,"3":7,"4":3,"5":1,"6":4,"7":7,"8":3,"9":5},"OKOPROD_LEAF_FLAG":{"0":"Y","1":"Y","2":"N","3":"Y","4":"Y","5":"Y","6":"Y","7":"Y","8":"Y","9":"Y"},"OKOPROD_VALID_FROM":{"0":"2020-01-01T00:00:00","1":"2020-01-01T00:00:00","2":"2020-01-01T00:00:00","3":"2022-01-01T00:00:00","4":"2020-01-01T00:00:00","5":"2020-01-01T00:00:00","6":"2020-01-01T00:00:00","7":"2022-01-01T00:00:00","8":"2020-01-01T00:00:00","9":"2020-01-01T00:00:00"},"OKOPROD_VALID_TO":{"0":"3000-01-01T00:00:00","1":"3000-01-01T00:00:00","2":"3000-01-01T00:00:00","3":"3000-01-01T00:00:00","4":"3000-01-01T00:00:00","5":"3000-01-01T00:00:00","6":"3000-01-01T00:00:00","7":"3000-01-01T00:00:00","8":"3000-01-01T00:00:00","9":"3000-01-01T00:00:00"},"OKOPROD_INSERTED_DATETIME":{"0":"2021-11-18T14:32:11","1":"2021-11-18T14:32:11","2":"2021-11-18T14:32:11","3":"2022-06-28T00:00:00","4":"2021-12-22T00:00:00","5":"2021-12-14T17:22:34","6":"2021-11-18T14:32:11","7":"2022-06-29T00:00:00","8":"2021-11-18T14:32:11","9":"2021-11-18T14:32:11"},"OKOPROD_UPDATED_DATETIME":{"0":"2021-11-18T14:32:11","1":"2021-11-18T14:32:11","2":"2021-11-18T14:32:11","3":"2022-06-28T00:00:00","4":"2021-12-22T00:00:00","5":"2021-12-14T17:22:34","6":"2021-11-18T14:32:11","7":"2022-06-29T00:00:00","8":"2021-11-18T14:32:11","9":"2021-11-18T14:32:11"},"INSERT_PROCESS_KEY":{"0":12028621,"1":12028621,"2":12028621,"3":12028621,"4":12028621,"5":12028621,"6":12028621,"7":12028621,"8":12028621,"9":12028621},"INSERT_TASKINS_KEY":{"0":143928354,"1":143928354,"2":143928354,"3":143928354,"4":143928354,"5":143928354,"6":143928354,"7":143928354,"8":143928354,"9":143928354},"_timestamp":{"0":"2024-05-02T05:03:14","1":"2024-05-02T05:03:14","2":"2024-05-02T05:03:14","3":"2024-05-02T05:03:14","4":"2024-05-02T05:03:14","5":"2024-05-02T05:03:14","6":"2024-05-02T05:03:14","7":"2024-05-02T05:03:14","8":"2024-05-02T05:03:14","9":"2024-05-02T05:03:14"}}
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
