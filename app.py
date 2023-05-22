import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("title is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''
 a + a r^1 + a r^2 + a r^3 ''')

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number',0,50)
                                 


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male", "Female"])

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
