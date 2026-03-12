# Import Groq library to interact with Groq LLM API
from groq import Groq

import os                          # To read environment variables 
from dotenv import load_dotenv     # To load variables from .env file 

load_dotenv()  # Loading variables from .env file into environment

client = Groq(api_key=os.getenv("GROQ_API_KEY"))   # os.getenv reads the Groq API Key

def ask_groq(question):  # This function sends a question to Groq AI

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":    "user",      # The one who is asking
                "content": question     # Asking question to AI
            }
        ],
        model="llama-3.1-8b-instant"
    )

    answer = chat_completion.choices[0].message.content  # Extracting AI generated response

    return answer   # Sending it to Flask backend