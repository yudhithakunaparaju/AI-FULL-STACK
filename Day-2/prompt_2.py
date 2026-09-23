import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"defination of ai in 2 lines and 3 types of aipython  "
        }
    ]
)
print(response["message"]["content"])