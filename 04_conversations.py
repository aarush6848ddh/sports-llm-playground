from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


messages = [                                                                              
      {"role": "system", "content": "You are a helpful assistant that provides information about sports."}                                                                           
  ]

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the conversation.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content
    print(f"Assistant: {reply}")

    messages.append({"role": "assistant", "content": reply})
