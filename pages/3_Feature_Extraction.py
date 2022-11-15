import streamlit as st

if 'scaledData' in st.session_state:
    st.write(st.session_state['scaledData'])
else:
    st.subheader('Empty data')
    st.text("Please run previous step first, that is data preparation.")