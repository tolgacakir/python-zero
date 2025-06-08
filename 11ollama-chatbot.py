from ollama import chat
messages =[]
while True:
    message = input("Enter your message: ")

    messages.append({"role": "user", "content": message})
    reply = chat(model='qwen2.5:14b', messages = messages)
    messages.append({"role": "assistant", "content": reply.message.content})
    
    print(reply.message.content)