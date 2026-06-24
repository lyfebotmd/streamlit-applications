import streamlit as st

import pandas as pd

 

st.title("Marks Chart")

 

data = {

    "Student": ["Amit", "Ravi", "Neha", "Priya"],

    "Marks": [85, 72, 90, 66]

}

 

df = pd.DataFrame(data)

 

st.dataframe(df)

st.bar_chart(df.set_index("Student"))