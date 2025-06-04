import streamlit as st
import pandas as pd
import numpy as np

st.write('DataFrame')
st.write(pd.DataFrame({
    'col 1': [1, 2, 3, 4],
    'col 2': [10, 20, 30, 40]
}))

st.write('Random DataFrame')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f'col {i+1}' for i in range(20)]
)
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write('Random Table')
st.table(dataframe.style.highlight_max(axis=0))