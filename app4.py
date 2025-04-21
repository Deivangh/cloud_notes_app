from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# Database connection (PythonAnywhere MySQL)
db = mysql.connector.connect(
    host="Deivangh.mysql.pythonanywhere-services.com",
    user="Deivangh",
    password="Jaahnavi30$",
    database="Deivangh$notes_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    cursor.execute("INSERT INTO notes (title, content, created_at) VALUES (%s, %s, NOW())", (title, content))
    db.commit()
    return redirect('/view')

@app.route('/view')
def view_notes():
    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()
    return render_template('view_notes.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

