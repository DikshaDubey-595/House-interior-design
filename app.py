from flask import Flask, render_template, request
import sqlite3

# Database create
def init_db():
    conn = sqlite3.connect('interior.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    ''')

    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)

#  Home
@app.route('/')
def home():
    return render_template('index.html')

#  Contact form
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = sqlite3.connect('interior.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO contacts (name, email, message)
    VALUES (?, ?, ?)
    ''', (name, email, message))

    conn.commit()
    conn.close()

    return f"Thank you {name}, your message has been saved ✅"

#  ADMIN PANEL (FIXED)
@app.route('/admin')
def admin():
    conn = sqlite3.connect('interior.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()

    conn.close()

    return render_template('admin.html', contacts=data)

#  Other pages
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

#  Run server
if __name__ == '__main__':
    app.run(debug=True)
    