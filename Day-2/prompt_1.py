import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"5 best animes"
        }
    ]
)
print(response["message"]["content"])