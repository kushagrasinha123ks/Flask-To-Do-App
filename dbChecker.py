import sqlite3
from os.path import exists

# Check if the database file exists, create if not
if not exists("todos.db"):
    open("todos.db", "w").close()

# Connect to the database
connection = sqlite3.connect("todos.db")
cursor = connection.cursor()

# Ensure the "todos" table exists
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "todos" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "todo" TEXT,
            "date" TEXT,
            "time" TEXT,
            "status" TEXT DEFAULT 'False',
            "editDate" TEXT,
            "editTime" TEXT
        );
    """)
    connection.commit()
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    connection.close()
