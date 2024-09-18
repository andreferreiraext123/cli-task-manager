from datetime import datetime
import os
from time import sleep
import sqlite3

DB_NAME = 'tasks_storage.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DB_NAME)

def initialize_db():
    """Create the tasks table if it doesn't exist."""
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()

def show_menu():
    print("\n-----Task Manager----")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Clear Screen")
    print("5. Exit")
    print("------------------------\n")

def add_task():
    task = input("\nEnter a description task (limit 100): ")[:100]
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (description) VALUES (?)', (task,))
        conn.commit()
    print("Task added successfully.")

def show_tasks():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, description, created_at FROM tasks ORDER BY created_at DESC')
        rows = cursor.fetchall()
        if rows:
            print("----List of Tasks----")
            for row in rows:
                print(f"Date: {row[2]} Task ID {row[0]}: {row[1]}")
        else:
            print("\n----List of Tasks----")
            print("No tasks available.")

def delete_task():
    try:
        task_id = int(input("\nEnter the task ID to delete: "))
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
            if cursor.rowcount > 0:
                conn.commit()
                print("Task deleted successfully.")
            else:
                print("\nError:\nNo task found with the given ID.")
    except ValueError:
        print("Error:\nInvalid input. Please enter a valid task ID.")

def clear_screen():
    n = 5
    while n > 0:
        print(f"Cleaning in {n}")
        n -= 1
        sleep(0.5)
    if os.name == 'nt':  # Windows
        os.system('cls')  # Clear the screen
        os.system('powershell -command Clear-History')
