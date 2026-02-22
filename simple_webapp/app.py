import streamlit as st
import pandas as pd
import numpy as np


##Title of the application
st.title("This is Streamlit")


##Display a simple text
st.write("This is a simple text")

##create a dataframe
df = pd.DataFrame({
    '1st col': [1, 2, 3, 4],
    '2nd col': [10, 20, 30, 40]
})

##show th dataframe
st.write("The new dataframe")
st.write(df)

##Create a linechart
data = pd.DataFrame(np.random.randn(20,3),columns=['a', 'b', 'c'])
st.line_chart(data)