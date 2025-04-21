from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Path to SQLite database
DB_PATH = 'notes.db'

# Create table if it doesn't exist
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

init_db()

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        conn.commit()
    return redirect('/view')

@app.route('/view')
def view_notes():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
        notes = cursor.fetchall()
    return render_template('view_notes.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))


