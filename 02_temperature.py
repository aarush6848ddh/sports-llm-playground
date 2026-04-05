from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

for temp in [0.0, 0.7, 1.5]:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides information about sports."},
            {"role": "user", "content": "Describe Lebron James' legacy in one sentence."}
        ],
        # temperature controls the randomness of the output. A higher value (e.g., 0.7) will make the output more creative, while a lower value (e.g., 0.0) will make result in a more deterministic output.
        temperature=temp
    )

    print(f"Temperature: {temp}")                                                                            
    print(response.choices[0].message.content)                                                               
    print("---")   


"""
Responses:

Temperature: 0.0
Lebron James' legacy is that of a transcendent basketball player and philanthropist 
who has dominated the sport for nearly two decades, earning numerous accolades, 
including four NBA championships and four MVP awards, while also making a lasting 
impact off the court through his charitable endeavors and social activism.
---
Temperature: 0.7
Lebron James' legacy is that of a transcendent basketball player and devoted 
philanthropist who has cemented his status as one of the greatest players in NBA 
history through his unmatched combination of on-court dominance, off-court 
activism, and lasting impact on the sport and society.
---
Temperature: 1.5
Lebron James' legacy is that of a transcendent basketball player and dedicated 
philanthropist, hailed as one of the greatest players of all time, with a storied 
20-year career marked by four NBA championships, four MVP awards, and a lasting 
impact on and off the court.
---
"""