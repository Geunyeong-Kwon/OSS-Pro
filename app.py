import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import graphviz as graphviz

st.title("title is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''
 a + a r^1 + a r^2 + a r^3 ''')

st.checkbox('yes')
st.button('Click', key='button1')
st.radio('Pick your gender', ['Male', 'Female'], key='radio1')
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number',0,50)
                                 
st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.tet_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click",key='button2')
st.sidebar.radio("Pick your gender",["Male", "Female"],key='radio2')

container = st.container()
container.write("This is written inside the container")
st.write("This is written outside the container")

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df = pd.DataFrane(
 np.random.randn(10,2),
 columns=['x','y'])
st.line_chart(df)

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')

df = pd.DataFrame(np.random.randn(500,2) / [50,50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)
