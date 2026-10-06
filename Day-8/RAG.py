from sentence_transformers import SentenceTransformer
import chromadb, ollama ,streamlit as st
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")
model=load_model()
st.title ("ChatBot")
if "messages" not in st.session_state:
    st.session_state.messages = []
with st.sidebar:
    st.header("Chat settings😀")
    personalities={
                 "kid👶":"Give the answers like you are explaining to a 5 year old kid.Give the answer in 2-3 lines only",
                 "Professor🧑‍🏫":"You are an IIT professor.Explain the topics using correct terminology.Give the answer in 2-3 lines only",
                 "Student😀":"You are an IIt student.Explain the topics like student or like a friend.Give the answers in 2-3 lines only "
                 } # personality
    personality=st.selectbox("Select a personality",personalities.keys())
    top_k=st.slider("Selct no of results",min_value=1,max_value=5,value=3)
    uploaded_file=st.file_uploader("Upload a file")
    if uploaded_file:
        text=uploaded_file.read().decode("utf-8")        
        with st.expander("Preview"):
            st.text(text)    
#file_name="sample.txt"
#with open(file_name,"r") as file:
#    text=file.read()

#Chunking
        chunks=[]
        chunk_size=100
        chunk_overlap=20
        step=chunk_size-chunk_overlap   #100 - 20 =30
        for i in range (0,len(text),step):
            chunk=text[i:i+chunk_size]   #(0 - 100) after jumps to(100 - 200)
            chunks.append(chunk)   

        #Embedding
        embeddings=model.encode(chunks)
        #print(embeddings[0])
        #print(embeddings.shape)

        #Vector DB
        client=chromadb.PersistentClient(path="./chroma_db")
        collection=client.get_or_create_collection(name="My_Documents")
        ids=[]
        for i in range(len(chunks)):
            ids.append(f"{uploaded_file}_{i}")

        collection.add(
            documents=chunks,
            ids=ids,
            embeddings=embeddings.tolist()
        )
        #res=collection.get()
        #chunk1=collection.get(ids=['sample.txt'])
        #print(chunk1)

#Query Phase
    st.subheader("Chat options")
    with st.container():
        if st.button("Clear Chat"):
            st.session_state.messages=[]
            st.success("Chat history deleted...")
    with st.expander("Chat History"):
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])        
question=st.chat_input("Question:")
if question:
    if uploaded_file:
        q_embedding=model.encode(question)
        results=collection.query(
            query_embeddings=[q_embedding.tolist()],
            n_results=top_k
        )
        retrieved_chunks=(results['documents'][0])
        retrieved_ids=results["ids"][0]
            #print(retrieved_chunks)
            #for i in range(len(results['documents'][0])):
            #    print(f"Chunk{i+1}")
            #    print(results['documents'][0][1])
        context='\n'.join(retrieved_chunks)
            #print(context)

            #Prompt
        prompt = f'''
        Answer the question using the context given below only.
        Question:{question}
        Context:{context}
        Answer:
        '''
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[{"role":"user",
                    "content":prompt}]
        )
        st.write (response["message"]["content"])
    else:
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