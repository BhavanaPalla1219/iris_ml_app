import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Simple Streamlit Webpage Example')

user_input = st.text_input('Enter some text:', 'Hello, Streamlit!')


num_input = st.slider('Select a number:', 0, 100, 25)


st.write(f'You entered: {user_input}')
st.write(f'You selected: {num_input}')


data = pd.DataFrame({
    'x': np.arange(0, 10),
    'y': np.random.randint(0, 100, 10)
})

st.subheader('Sample Data')
st.write(data)


st.subheader('Sample Data Plot')
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'], marker='o', linestyle='-')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Sample Line Plot')


st.pyplot(fig)
