import sqlite3
import os

# Hardcoded credentials (bad practice)
SECRET_KEY = "super_secret_password_123"
DB_PASSWORD = "admin123"
API_KEY = "sk-abc123def456ghi789"

def get_user(username):
    # SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

def run_command(user_input):
    # Command injection vulnerability
    os.system("ls " + user_input)

def read_file(filename):
    # Path traversal vulnerability
    with open("/var/www/" + filename, "r") as f:
        return f.read()

def login(username, password):
    # No password hashing
    if password == DB_PASSWORD:
        return True
    return False