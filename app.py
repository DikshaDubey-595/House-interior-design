from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# ✅ ABOUT DETAILS ROUTE (IMPORTANT)
@app.route('/about-details')
def about_details():
    return render_template('about-details.html')

@app.route('/interior-design')
def interior_design():
    return render_template('interior-design.html')

@app.route('/interior-styling')
def interior_styling():
    return render_template('interior-styling.html')

@app.route('/interior-architecture')
def interior_architecture():
    return render_template('interior-architecture.html')

# Contact
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = sqlite3.connect('interior.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)',
                   (name, email, message))

    conn.commit()
    conn.close()

    return f"Thank you {name}, your message has been saved ✅"

# Run
if __name__ == "__main__":
    app.run(debug=True)