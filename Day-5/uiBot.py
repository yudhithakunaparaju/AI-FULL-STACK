import ollama
import streamlit as st
st.title(":rainbow[***CHAT BOT!!***]🧧") # to add color ": color[title]",*=italic,**=bold,***=ita&bold
                                                                #=large txt,##less large txt,###=smaller txt
with st.sidebar:
        personalities={
            "kid👶":"Give the answers like you are explaining to a 5 year old kid.Give the answer in 2-3 lines only",
            "Professor🧑‍🏫":"You are an IIT professor.Explain the topics using correct terminology.Give the answer in 2-3 lines only",
            "Student😀":"You are an IIt student.Explain the topics like student or like a friend.Give the answers in 2-3 lines only "
        } # personality
        personality=st.selectbox("Select a personality",personalities.keys())
        if st.button("Clear Chat😅"):
            st.session_state.messages=[]
            st.success("Chat cleared successfully👻")
        st.header("Chat settings😀")
        uploaded_file=st.file_uploader("Upload your file📂...")
        if uploaded_file:
            st.success("File uploaded successfully✅...")
            with st.expander("Preview"):
                context=uploaded_file.read().decode("utf-8")
                st.text(context)    # only use txt file
                   
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:     #it helps to save history
    with st.chat_message(msg["role"]):
        st.write("AI:", msg["content"])

question = st.chat_input("Question: ")

if question:
    with st.chat_message("user"):
        st.write("You:", question)

    st.session_state.messages.append(             
        {"role":"user",
         "content":question}
         )
    with st.spinner("Thinking 🤔💭....."):# to load in chat
        response=ollama.chat(
            model="llama3.2:3b",
            messages=[{
                "role":"system", "content": personalities[personality]
                }]+st.session_state.messages
            )
    st.session_state.messages.append(
        {"role":"assistant",
         "content":response["message"]["content"]}
    )
    with st.chat_message("assistant"):# to get emoij for assistant
        st.write("AI:", response["message"]["content"])
        uploaded_file=st.file_uploader("upload a file")    #to upload file
st.snow() 
st.balloons()       
    
    