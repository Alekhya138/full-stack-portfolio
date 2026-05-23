from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# -------------------------------
# DATABASE PATH
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "portfolio.db")

# -------------------------------
# CONNECT DATABASE
# -------------------------------
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# -------------------------------
# CREATE TABLE
# -------------------------------
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Run once
init_db()

# -------------------------------
# HOME PAGE
# -------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------------
# CONTACT FORM
# -------------------------------
@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = get_db_connection()

    conn.execute(
        "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )

    conn.commit()
    conn.close()

    return redirect('/')

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == '__main__':
    # Get the port from Render's environment, or default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    # Listen on 0.0.0.0 so Render can access it
    app.run(host="0.0.0.0", port=port, debug=True)