import streamlit as st
st.title("welcome to my first app")
st.write("Hello")
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
st.chat_input("Enter your message here...")
st.text_input("Enter your name", key="name")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
st.checkbox("check me out")
st.balloons()
st.subheader()