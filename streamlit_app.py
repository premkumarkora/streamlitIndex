import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('Prem Photo.png'))

st.header('PremKumar Kora')

st.info("Data scientist with expertise in creating, developing, testing and deploying data science algorithms to deliver meaningful insights and implement action-oriented solutions to complex business problems")

icon_size = 20


st_button('medium', 'https://consultkora.medium.com/', 'Read my Blogs', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/premkumarkora/', 'Follow me on LinkedIn', icon_size)
st_button('newsletter', 'https://sendfox.com/consultkora', 'Sign up for my Newsletter', icon_size)
st_button('cup', 'https://www.buymeacoffee.com/consultkora', 'Buy me a Coffee', icon_size)
