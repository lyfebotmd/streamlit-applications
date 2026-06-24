import streamlit as st

import pandas as pd

 

st.title("Student Marks Dashboard")

 

st.write("This app collects student details and displays marks summary.")

 

name = st.text_input("Student Name")

subject = st.selectbox("Subject", ["Python", "AI", "Data Science", "Machine Learning"])

marks = st.number_input("Marks", min_value=0, max_value=100)

 

if st.button("Generate Report"):

    if marks >= 50:

        result = "Pass"

        st.success("Student Passed")

    else:

        result = "Fail"

        st.error("Student Failed")

 

    data = {

        "Name": [name],

        "Subject": [subject],

        "Marks": [marks],

        "Result": [result]

    }

 

    df = pd.DataFrame(data)

 

    st.subheader("Student Report")

    st.dataframe(df)




