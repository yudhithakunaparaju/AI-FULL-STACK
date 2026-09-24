import ollama
msgs=[
    {
        "role":"user",          
        "content":"Give the answer in funny way in 2 lines only"
    }    
    ]
while True:
    question = input("Question: ")
    if question.lower() == "exit":
        break      
    msgs.append(             
        {"role":"user",
         "content":question}
    )
    response=ollama.chat(
        model="llama3.2:3b",
        messages=msgs
    )
    msgs.append(
        {"role":"assistant",
         "content":response["message"]["content"]}
    )
    
    print("AI:",response["message"]["content"])
print("Chat History: \n")    
for msg in msgs:
    if msg["role"]=="system":
        continue
    print(f"{msg['role'].capitalize()}: {msg['content']}")
