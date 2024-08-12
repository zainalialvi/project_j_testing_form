import streamlit as st

st.title("Project J Testing Form")

with st.form(key='testing_form'):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    gender = st.selectbox("Gender", ["Male", "Female"])
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.success("Form submitted successfully!")
