import streamlit as st

 

st.title("Registration Form")

 

with st.form("student_form"):

    name = st.text_input("Name")

    email = st.text_input("Email")

    course = st.selectbox("Course", ["Python", "AI", "DevOps"])

    submitted = st.form_submit_button("Register")

 

if submitted:

    st.success("Registration completed")

    st.write("Name:", name)

    st.write("Email:", email)

    st.write("Course:", course)