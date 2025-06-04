import streamlit as st
import pandas as pd
import numpy as np
import time

st.header('Basic Concepts')

st.write('DataFrame')
df = pd.DataFrame({
    'col 1': [1, 2, 3, 4],
    'col 2': [10, 20, 30, 40]
})
st.write(df)

st.write('Random DataFrame')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f'col {i+1}' for i in range(20)]
)
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write('Random Table')
st.table(dataframe.style.highlight_max(axis=0))

st.write('Random Line Chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.write('Random Map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

st.write('x^2 Slider')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.write('Text Input')
st.text_input("Your name", key="name")
st.session_state.name

st.write('Checkbox')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data

st.write('Selectbox')
option = st.selectbox(
    'Which number do you like best?',
     df['col 1'])
'You selected: ', option

st.write('Sidebar')
st.caption('See side')
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write('Columns')
left_column, right_column = st.columns(2)
left_column.button('Press me!')
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

st.write('Progress Bar')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)