import streamlit as st

#st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1:
    st.image("Image/Piyas.jpg")
with col2:
    st.title("Piyas Saha")
    content = '''Hi! This is Piyas Saha. I am graduated and post graduated from 
    Electrical and Electronic Engineering from KUET,Bangladesh. I work on DESCO as
    an Assistant Engineer.'''
    st.info(content)

content2= '''Feel free to contact with me if anything you want to ask me. I will answer.'''
st.write(content2)