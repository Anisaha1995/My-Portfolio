import streamlit as st

from email_send import send_email
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New Email from {user_email}

From {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit",key="button")
    if button:
        send_email(message)
        st.info("You message has been sent successfully.")

st.header("Connect with me")
cola,colb = st.columns([1,4],gap="small")
with cola:
    st.image("lk.png",width=50)
    st.write(f"[Click Here](https://www.linkedin.com/in/piyas-saha-b25830171/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BQP%2BOqfMhQXKgfyYeivzMkw%3D%3D)")
with colb:
    st.image("gs.png",width=50)
    st.write(f"[Click Here](https://scholar.google.com/citations?user=gxWV3REAAAAJ&hl=en)")