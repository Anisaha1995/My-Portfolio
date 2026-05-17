import streamlit as st
import pandas
#st.set_page_config(layout="wide")
col1,col2 = st.columns(2)
with col1:
    st.image("Image/Piyas.jpg")
with col2:
    st.title("Piyas Saha")
    content = '''I am a Power System Automation Engineer with a B.Sc. and M.Sc. in Electrical and Electronic Engineering from Khulna University of Engineering & Technology (KUET). I currently work at Dhaka Electric Supply Company Limited (DESCO), one of Bangladesh’s leading government-owned power distribution utilities.

At DESCO, I am involved in the operation and maintenance of Substation Automation Systems (SAS) and Remote Terminal Units (RTUs). I also played a key role in the installation and commissioning of the Supervisory Control and Data Acquisition (SCADA) system — the first initiative to automate the distribution system in Bangladesh.

My research interests include Wide Area Monitoring Systems (WAMS) and Smart Grids. During my postgraduate studies, I developed an algorithm for the optimal placement of Phasor Measurement Units (PMUs) and applied it to design a WAMS for the National Grid of Bangladesh.

I am particularly passionate about bridging research and practice to solve real-world challenges in modern power systems — especially in areas such as grid resilience, automation, and secure energy management.'''
    st.info(content)

content2= '''Feel free to contact with me if anything you want to ask me. I will answer.'''
st.write(content2)
df = pandas.read_csv("008 data.csv", sep = ";")
col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
with col3:
    for index,row in df[:11].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Image/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[11:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Image/" + row["image"])
        st.write(f"[Source Code]({row['url']})")