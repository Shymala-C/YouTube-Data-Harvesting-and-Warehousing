import streamlit as st
st.title('youtube project')
name=st.text_input('enter your channel:')
a=st.button('enter')
if a:
    st.write(f'hi {name},youtube project')
