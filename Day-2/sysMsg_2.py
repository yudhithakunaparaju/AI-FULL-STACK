import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"explain me as a 5 years old child in 2 to 3 lines"
        },
        {
            "role":"user",
            "content":"explain ai in 6 lines"
        }
    ]
)
print(response["message"]["content"])