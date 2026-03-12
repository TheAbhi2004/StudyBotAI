# Importing Flask framework 
from flask import Flask, render_template, request, jsonify 

from groq_client import ask_groq   # Importing Groq AI function 

from database import save_chat     # Importing save_chat function

app = Flask(__name__)   # Creating Flask application instance 


# ---------------------
# Route 1 : Home Page 
# --------------------- 

@app.route("/")  # This route loads the webpage
def home():
    return render_template("index.html") 

# -------------------------- 
# Route 2: AI Question API
# -------------------------- 

@app.route("/ask", methods=["POST"])    # This route receives user question
def ask():
    data = request.get_json()           # Get question sent from JavaScript

    question = data.get("question")

    answer = ask_groq(question)         # Sending question to Groq AI

    save_chat(question, answer)         # Saving the chat into database

    return jsonify({                    # Sending AI answer back to front-end
        "answer": answer
    })

# --------------------
# Start Flask Server
# --------------------

if __name__ == "__main__":
    app.run(debug=True)