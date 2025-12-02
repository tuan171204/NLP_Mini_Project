from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime
from nlp_model import analyze_sentiment

app = Flask(__name__)
DB_NAME = 'sentiment.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  input_text TEXT,
                  sentiment_label TEXT,
                  timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_to_history(text, label):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO history (input_text, sentiment_label, timestamp) VALUES (?, ?, ?)",
              (text, label, time_now))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT input_text, sentiment_label, timestamp FROM history ORDER BY id DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    current_result = None
    current_text = ""
    label_raw = ""
    if request.method == 'POST':
        current_text = request.form.get('user_text', '').strip()
        
        if current_text:
            label_raw, display_label, score = analyze_sentiment(current_text)
            current_result = f"{display_label} (Độ tin cậy: {score:.2f})"
            
            save_to_history(current_text, display_label)

    history_data = get_history()
    return render_template('index.html', history=history_data, result=current_result, last_text=current_text, label_raw=label_raw)

if __name__ == '__main__':
    init_db()
    app.run(debug=True) 