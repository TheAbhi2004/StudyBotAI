import mysql.connector  

def get_db_connection():
    conn = mysql.connector.connect(
        host = "localhost",      
        user = "root" ,          
        password = "Abhi@2004",   
        database = "studybot"     
    )

    return conn

def save_chat(question, answer):
    conn = get_db_connection()    
    cursor = conn.cursor()          

    query = """ 
    INSERT INTO chats (question, answer) 
    VALUES (%s, %s) 
    """

    cursor.execute(query, (question, answer)) 
    conn.commit()     
    cursor.close()    
    conn.close()    


def get_chat_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM chats ORDER BY created_at DESC"
    cursor.execute(query) 
    chats = cursor.fetchall()
    cursor.close()
    conn.close()

    return chats