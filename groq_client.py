from groq import Groq
import os                          
from dotenv import load_dotenv     

load_dotenv()  

client = Groq(api_key=os.getenv("GROQ_API_KEY"))   

def ask_groq(question): 

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",      
                "content": question    
            }
        ],
        model="llama-3.1-8b-instant"
    )

    answer=chat_completion.choices[0].message.content  

    return answer   