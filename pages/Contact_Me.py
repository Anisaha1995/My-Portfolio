import streamlit as st
from streamlit import button

st.header("Contact Me")

with st.form(key="email_form"):
    st.text_input("Your email address")
    st.text_area("Your Message")
    st.form_submit_button("Submit",key="button")
    if button:
        print("Pressed")