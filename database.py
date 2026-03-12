# Importing MySQL connector library 
import mysql.connector  

# ---------------------------------------
# Function to create database connection
# ---------------------------------------

def get_db_connection():

    # Connecting to MySQL database 
    conn = mysql.connector.connect(
        host = "localhost",       # MySQL server address
        user = "root" ,           # MySQL username 
        password = "Abhi@2004",   # MySQL password
        database = "studybot"     # Database created in MySQL 
    )

    return conn

# ------------------------------------
# Function to save chat into database
# ------------------------------------

def save_chat(question, answer):
    conn = get_db_connection()      # Creating connection

    cursor = conn.cursor()          # Creating cursor to execute SQL queries

    query = """ 
    INSERT INTO chats (question, answer) 
    VALUES (%s, %s) 
    """

    cursor.execute(query, (question, answer))   # Executes the query 

    conn.commit()     # Saving all the changes

    cursor.close()    # ✅ Fixed: cursor was never closed in save_chat
    conn.close()      # Closing the connection

# ----------------------------- 
# Function to get chat history
# -----------------------------

def get_chat_history():
    conn = get_db_connection()

    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM chats ORDER BY created_at DESC"

    cursor.execute(query) 

    chats = cursor.fetchall()

    cursor.close()
    conn.close()

    return chats