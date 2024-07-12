
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('Backup_Animal_Taxonomy_Db.db')
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute("SELECT * FROM animal_details")
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)