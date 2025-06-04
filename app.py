import streamlit as st
import pandas as pd
import numpy as np
import time

st.header('Basic Concepts')

st.subheader('DataFrame')
df = pd.DataFrame({
    'col 1': [1, 2, 3, 4],
    'col 2': [10, 20, 30, 40]
})
st.write(df)

st.subheader('Random DataFrame')
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=[f'col {i+1}' for i in range(20)]
)
st.dataframe(dataframe.style.highlight_max(axis=0))

st.subheader('Random Table')
st.table(dataframe.style.highlight_max(axis=0))

st.subheader('Random Line Chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader('Random Map')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

st.subheader('x^2 Slider')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.subheader('Text Input')
st.text_input("Your name", key="name")
st.session_state.name

st.subheader('Checkbox')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    chart_data

st.subheader('Selectbox')
option = st.selectbox(
    'Which number do you like best?',
     df['col 1'])
'You selected: ', option

st.subheader('Sidebar')
st.write('See side')
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.subheader('Columns')
left_column, right_column = st.columns(2)
left_column.button('Press me!')
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

st.subheader('Progress Bar')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(5):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(20 * (i + 1))
    time.sleep(0.1)


st.header('Advanced Concepts')

st.subheader('Caching')
@st.cache_data
def long_running_function():
    pass

st.subheader('Session State')
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.write(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])
st.write("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

st.subheader('Connections')
# conn = st.connection("my_database")
# sql_df = conn.query("select * from my_table")
# st.dataframe(sql_df)


st.header('Additional Features')

st.subheader('Pages')
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")
pg = st.navigation([main_page, page_2, page_3])
pg.run()

st.subheader('Static File Serving')
st.image('static/cat.png')