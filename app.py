
from flask import Flask, render_template, request, jsonify

from groq_client import ask_groq
from database import (
    create_conversation,
    save_message,
    get_conversations,
    get_messages
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Create a new conversation
@app.route("/new_chat", methods=["POST"])
def new_chat():
    conversation_id = create_conversation()

    return jsonify({
        "conversation_id": conversation_id,
        "title": "New Chat"
    })


# Get all conversations for the sidebar
@app.route("/conversations", methods=["GET"])
def conversations():
    chats = get_conversations()

    return jsonify({
        "conversations": chats
    })


# Load messages from a selected conversation
@app.route("/conversation/<int:conversation_id>", methods=["GET"])
def load_conversation(conversation_id):
    messages = get_messages(conversation_id)

    return jsonify({
        "messages": messages
    })


# Ask StudyBot a question
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question")
    conversation_id = data.get("conversation_id")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Create a conversation if one wasn't selected
    if not conversation_id:
        conversation_id = create_conversation()

    # Save the user's question
    save_message(conversation_id, "user", question)

    # Get the AI response
    answer = ask_groq(question)

    # Save the AI response
    save_message(conversation_id, "assistant", answer)

    return jsonify({
        "answer": answer,
        "conversation_id": conversation_id
    })


if __name__ == "__main__":
    app.run(debug=True)
