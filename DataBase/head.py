import sqlite3
import time
import os

DB_NAME = "commands.db"
LOGS_DIR = "logs"

# Функции для работы с базой данных
def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS commands (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS arguments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command_name TEXT NOT NULL,
            argument TEXT NOT NULL,
            description TEXT NOT NULL,
            FOREIGN KEY (command_name) REFERENCES commands (name)
        )
    ''')
    conn.commit()
    conn.close()

def add_command(name, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO commands (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

def add_argument(command_name, argument, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO arguments (command_name, argument, description) VALUES (?, ?, ?)", (command_name, argument, description))
    conn.commit()
    conn.close()

def search_commands(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, description FROM commands WHERE name LIKE ? OR description LIKE ?", (f'%{keyword}%', f'%{keyword}%'))
    results = cursor.fetchall()
    conn.close()
    return results

def get_arguments(command_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT argument, description FROM arguments WHERE command_name=?", (command_name,))
    results = cursor.fetchall()
    conn.close()
    return results

def log_command(command, result):
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)
    log_file = os.path.join(LOGS_DIR, f"log_{int(time.time())}.txt")
    with open(log_file, 'w') as file:
        file.write(f"Command:\n{command}\n\nResult:\n{result}\n")

def get_logs():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)
    return [f for f in os.listdir(LOGS_DIR) if os.path.isfile(os.path.join(LOGS_DIR, f))]

def read_log(log_file):
    with open(log_file, 'r') as file:
        return file.read()


