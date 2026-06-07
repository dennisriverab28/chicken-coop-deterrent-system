import sqlite3
from datetime import datetime

DB_NAME = "coop_log.db"

def log_event(event, context=""):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        event TEXT,
        context TEXT
    )''')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO logs (timestamp, event, context) VALUES (?, ?, ?)", (now, event, context))
    conn.commit()
    conn.close()
