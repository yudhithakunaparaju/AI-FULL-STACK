import ollama
import streamlit as st
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:     #it helps to save history 
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write("You:", msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write("AI:", msg["content"])

question = st.chat_input("Question: ")

if question:
    with st.chat_message("user"):
        st.write("You:", question)

st.session_state.messages.append(             
        {"role":"user",
         "content":question}
    )
with st.spinner(">_< ....."):# to load in chat
    response=ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
    )
st.session_state.messages.append(
        {"role":"assistant",
         "content":response["message"]["content"]}
    )
    
with st.chat_message("assistant"):# to get emoij for assistant
    st.write("AI:", response["message"]["content"])

uploaded_file=st.file_uploader("upload a file")    #to upload file
if uploaded_file:
    st.write("Your file is uploaded")
    context=uploaded_file.read().decode("utf-8")
    st.text(context)    # only use txt file
    st.sidebar()
    