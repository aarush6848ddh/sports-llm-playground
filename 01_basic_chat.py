from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Create a chat completion
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that provides information about sports."},
        {"role": "user", "content": "Who won the NBA championship in 2022?"}
    ]
)

print(response.choices[0].message.content)