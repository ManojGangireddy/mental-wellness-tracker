# mental_wellness_tracker/database.py
import sqlite3
from datetime import datetime

DB_NAME = "journal_entries.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            polarity REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_entry(entry, sentiment, polarity):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO journal (entry, sentiment, polarity)
        VALUES (?, ?, ?)
    ''', (entry, sentiment, polarity))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT entry, sentiment, polarity, timestamp FROM journal ORDER BY timestamp ASC')
    rows = c.fetchall()
    conn.close()
    return rows

# Initialize the DB when this file is first run
init_db()
