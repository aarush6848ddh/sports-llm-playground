from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables    
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompts = [
    "What is the NBA",
    "Why is there a western and eastern conference in the NBA?",
    "Describe each position in basketball and the role they play on the court.",
]

total_tokens = 0

for prompt in prompts:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides information about sports."},
            {"role": "user", "content": prompt}
        ]
    )

    print(f"Prompt: {prompt}")                                                                            
    print(response.choices[0].message.content)   
    print(f"Prompt tokens: {response.usage.prompt_tokens}")                                   
    print(f"Completion tokens: {response.usage.completion_tokens}")                           
    print(f"Total tokens: {response.usage.total_tokens}")                                                               
    print("---")

    total_tokens += response.usage.total_tokens

print(f"Total tokens used across all prompts: {total_tokens}")