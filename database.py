import sqlite3
import bcrypt
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "journal.db")

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT, value TEXT)")
    conn.commit()
    conn.close()

def set_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", ("password", hashed))
    conn.commit()
    conn.close()

def check_password(password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT value FROM settings WHERE key = ?", ("password",))
    result = cur.fetchone()
    
    if result is None:
        conn.close()
        return False
    elif bcrypt.checkpw(password.encode(), result[0].encode()):
        conn.close()
        return True
    else:
        conn.close()
        return False
    
def has_password():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT value FROM settings WHERE key = ?", ("password",))
    result = cur.fetchone()
    
    if result is None:
        conn.close()
        return False
    else:
        conn.close()
        return True
    
def save_setting(key, value):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def get_setting(key):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT value FROM settings WHERE key = ?", (key,))
    result= cur.fetchone()
    if result is None:
        conn.close()
        return None
    else:
        conn.close()
        return result[0]
    
def reset_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM settings")
    conn.commit()
    conn.close()

    
