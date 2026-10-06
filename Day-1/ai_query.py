import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"explain about the difference between supervised and unsupervised learning in 2 lines"
        }
    ]
)
print(response["message"]["content"])