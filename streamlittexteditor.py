import streamlit as st
import os

st.write("hello")
st.write('5 4 3 2 1')
st.write({"key":"value"})
st.write(True)
7*8
"hello" if False else "bye"
pressed = st.button('press')
print('first:' , pressed)
pressed1 = st.button('yay')
print('second:',pressed1)
st.title("super title")
st.header('header')
st.subheader('why')
st.markdown('markdown _1_')
st.caption('small text')
code_example = """
def greet (name):
    print('hello', name)
"""
st.code(code_example, language="py")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "goku-super-saiyan-rose-dragon-ball-thumb.jpg"))

