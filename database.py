import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Create a new conversation
def create_conversation(title="New Chat"):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO conversations (title)
        VALUES (%s)
    """

    cursor.execute(query, (title,))
    conversation_id = cursor.lastrowid

    conn.commit()
    cursor.close()
    conn.close()

    return conversation_id


# Save one message in a conversation
def save_message(conversation_id, role, content):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO messages (conversation_id, role, content)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (conversation_id, role, content))

    # Update the conversation's latest activity time
    update_query = """
        UPDATE conversations
        SET updated_at = CURRENT_TIMESTAMP
        WHERE id = %s
    """

    cursor.execute(update_query, (conversation_id,))

    # Use the first user message as the conversation title
    if role == "user":
        title_query = """
            UPDATE conversations
            SET title = %s
            WHERE id = %s AND title = 'New Chat'
        """

        title = content[:50]
        cursor.execute(title_query, (title, conversation_id))

    conn.commit()
    cursor.close()
    conn.close()


# Get all conversations for the history sidebar
def get_conversations():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT id, title, created_at, updated_at
        FROM conversations
        ORDER BY updated_at DESC
    """

    cursor.execute(query)
    conversations = cursor.fetchall()

    cursor.close()
    conn.close()

    return conversations


# Get all messages belonging to one conversation
def get_messages(conversation_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT id, conversation_id, role, content, created_at
        FROM messages
        WHERE conversation_id = %s
        ORDER BY created_at ASC, id ASC
    """

    cursor.execute(query, (conversation_id,))
    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    return messages
