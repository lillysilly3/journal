import sqlite3
import bcrypt
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "journal.db")

class DatabaseClient():
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS settings (key TEXT, value TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS entries (date TEXT PRIMARY KEY, content TEXT, mood TEXT)")
        self.conn.commit()       

    def set_password(self, password):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.cur.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", ("password", hashed))
        self.conn.commit()

    def check_password(self, password):
        self.cur.execute("SELECT value FROM settings WHERE key = ?", ("password",))
        result = self.cur.fetchone()
        
        if result is None:
            return False
        elif bcrypt.checkpw(password.encode(), result[0].encode()):
            return True
        else:
            return False
        
    def has_password(self):
        self.cur.execute("SELECT value FROM settings WHERE key = ?", ("password",))
        result = self.cur.fetchone()
        
        if result is None:
            return False
        else:
            return True
        
    def save_setting(self, key, value):
        self.cur.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
        self.conn.commit()

    def get_setting(self, key):
        self.cur.execute("SELECT value FROM settings WHERE key = ?", (key,))
        result= self.cur.fetchone()
        if result is None:
            return None
        else:
            return result[0]
        
    def reset(self):
        self.cur.execute("DELETE FROM settings")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def save_entry(self, date, content, mood):
        self.cur.execute("INSERT OR REPLACE INTO entries (date, content, mood) VALUES (?, ?, ?)", (date, content, mood))
        print (date, content, mood)
        self.conn.commit()

    def get_entry(self, date):
        self.cur.execute("SELECT content, mood FROM entries WHERE date = ?", (date,))
        result = self.cur.fetchone()
        print (result)
        if result is None:
            return None
        else:
            return result
        
    #Fetching months worth entries
    def get_entries_for_month(self, year, month):
        month_str = f"{year}-{month:02d}"
        self.cur.execute("SELECT date, mood FROM entries WHERE date LIKE ?", (f"{month_str}%",))
        results = self.cur.fetchall()
        return {row[0]: (True, row[1]) for row in results}

