import sqlite3
import secrets
from datetime import datetime
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

# Function to get the current date
def currentDate():
    return datetime.now().strftime("%d.%m.%y")

# Function to get the current time
def currentTime():
    return datetime.now().strftime("%H:%M")

# Route to display all todos
@app.route("/")
def index():
    try:
        connection = sqlite3.connect("todos.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM todos")
        todos = cursor.fetchall()
        connection.close()
        return render_template("index.html", todos=todos)
    except sqlite3.Error as e:
        return f"Database error: {e}", 500

# Route to add a new todo
@app.route("/add/<todo>")
def add(todo):
    try:
        connection = sqlite3.connect("todos.db")
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO todos(todo, date, time) VALUES (?, ?, ?)',
            (todo, currentDate(), currentTime())
        )
        connection.commit()
        connection.close()
        return redirect("/")
    except sqlite3.Error as e:
        return f"Database error: {e}", 500

# Route to mark a todo as complete
@app.route("/check/<int:id>")
def check(id):
    try:
        connection = sqlite3.connect("todos.db")
        cursor = connection.cursor()
        cursor.execute('UPDATE todos SET status = "True" WHERE id = ?', (id,))
        cursor.execute('UPDATE todos SET editDate = ? WHERE id = ?', (currentDate(), id))
        cursor.execute('UPDATE todos SET editTime = ? WHERE id = ?', (currentTime(), id))
        connection.commit()
        connection.close()
        return redirect("/")
    except sqlite3.Error as e:
        return f"Database error: {e}", 500

# Route to unmark a todo
@app.route("/uncheck/<int:id>")
def uncheck(id):
    try:
        connection = sqlite3.connect("todos.db")
        cursor = connection.cursor()
        cursor.execute('UPDATE todos SET status = "False" WHERE id = ?', (id,))
        connection.commit()
        connection.close()
        return redirect("/")
    except sqlite3.Error as e:
        return f"Database error: {e}", 500

# Route to edit a todo
@app.route("/edit/<int:id>/<todo>")
def edit(id, todo):
    try:
        connection = sqlite3.connect("todos.db")
        cursor = connection.cursor()
        cursor.execute('UPDATE todos SET todo = ? WHERE id = ?', (todo, id))
        connection.commit()
        connection.close()
        return redirect("/")
    except sqlite3.Error as e:
        return f"Database error: {e}", 500

# Route to delete a todo
@app.route("/delete/<int:id>")
def delete(id):
    try:
        connection = sqlite3.connect("todos.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM todos WHERE id = ?", (id,))
        cursor.execute("UPDATE sqlite_sequence SET seq = seq - 1 WHERE name = 'todos'")
        connection.commit()
        connection.close()
        return redirect("/")
    except sqlite3.Error as e:
        return f"Database error: {e}", 500

# Error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Main entry point
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
