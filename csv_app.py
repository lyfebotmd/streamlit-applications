import streamlit as st

import pandas as pd

 

st.title("CSV Data Viewer")

 

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

 

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

 

    st.subheader("Dataset Preview")

    st.dataframe(df)

 

    st.subheader("Dataset Information")

    st.write("Rows and Columns:", df.shape)

 

    st.subheader("Column Names")

    st.write(df.columns.tolist())

 

    st.subheader("Summary Statistics")

    st.write(df.describe())




