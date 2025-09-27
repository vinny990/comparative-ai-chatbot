# database.py
import sqlite3
from datetime import datetime
import os

def init_db():
    db_path = os.getenv("DB_PATH", "responses.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS responses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  prompt TEXT,
                  openai_response TEXT,
                  claude_response TEXT,
                  gemini_response TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_response(prompt, openai_response, claude_response, gemini_response):
    db_path = os.getenv("DB_PATH", "responses.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute(
        "INSERT INTO responses (prompt, openai_response, claude_response, gemini_response, timestamp) "
        "VALUES (?, ?, ?, ?, ?)",
        (prompt, openai_response, claude_response, gemini_response, timestamp)
    )
    conn.commit()
    conn.close()
