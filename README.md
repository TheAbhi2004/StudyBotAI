# 🤖 StudyBotAI – AI Learning Companion

StudyBotAI is an **AI-powered study assistant** that helps users explore concepts, solve problems, and learn new topics instantly using **Large Language Models (LLMs)**.

The project integrates **Groq API (Llama 3.1)** with a **Flask backend** and stores chat history in **MySQL**.

---

## 🚀 Features

- 🤖 AI-powered question answering  
- ⚡ Fast responses using **Groq API**  
- 💬 Interactive chat interface  
- 🗂 Chat history stored in **MySQL database**  
- 🔐 Secure API key management using **python-dotenv**  
- 🎨 Modern and responsive UI  

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### AI Model
- Groq API (Llama 3.1)

### Database
- MySQL

### Frontend
- HTML  
- CSS  
- JavaScript  

### Python Libraries
- flask  
- groq  
- mysql-connector-python  
- python-dotenv  

---

## 📂 Project Structure

```
StudyBotAI
│
├── static
│   ├── style.css
│   └── script.js
│
├── templates
│   └── index.html
│
├── app.py
├── database.py
├── groq_client.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository

```bash
git clone https://github.com/TheAbhi2004/StudyBotAI.git
cd StudyBotAI
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5️⃣ Setup MySQL Database

Run the following SQL commands:

```sql
CREATE DATABASE studybot;

USE studybot;

CREATE TABLE chats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 6️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

```
User Question
      ↓
Frontend (HTML + JavaScript)
      ↓
Flask Backend
      ↓
Groq API (Llama 3.1)
      ↓
AI Response Generated
      ↓
Stored in MySQL
      ↓
Displayed in Chat UI
```

---

## 🔐 Environment Variables

| Variable | Description |
|--------|-------------|
| GROQ_API_KEY | API key used to access Groq LLM |

---

## 📌 Future Improvements

- 📄 PDF document question answering  
- 🧠 RAG-based study assistant  
- 👤 User authentication  
- 📊 Learning analytics dashboard  
- 🌙 Dark/Light mode toggle  

---

## 👨‍💻 Author

**Abhishek**

GitHub:  
https://github.com/TheAbhi2004

---

⭐ If you like this project, consider giving it a **star** on GitHub!
