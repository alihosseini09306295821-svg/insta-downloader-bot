import sqlite3

DB_NAME = "users.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(user_id, username, first_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO users(user_id, username, first_name)
    VALUES(?,?,?)
    """, (user_id, username, first_name))

    conn.commit()
    conn.close()


def total_users():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]

    conn.close()
    return count
