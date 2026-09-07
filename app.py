from flask import Flask, render_template, request, jsonify 
from groq_client import ask_groq 
from database import save_chat  

app = Flask(__name__)  

@app.route("/") 
def home():
    return render_template("index.html") 


@app.route("/ask", methods=["POST"])  
def ask():
    data = request.get_json()       
    question = data.get("question")
    answer = ask_groq(question)     
    save_chat(question, answer)    

    return jsonify({              
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)