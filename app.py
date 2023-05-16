import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male", "Female"])

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
