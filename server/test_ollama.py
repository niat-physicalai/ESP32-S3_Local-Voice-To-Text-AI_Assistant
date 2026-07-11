from ollama import chat

response = chat(
    model="qwen2.5:1.5b",
    messages=[
        {
            "role": "user",
            "content": "What is ESP32?"
        }
    ]
)

print(response["message"]["content"])