from flask import Flask, jsonify
from db import Database

app = Flask(__name__)
app.config['THREADS_PER_PAGE'] = 1

@app.route('/')
def index():
    db = Database()

    db.query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    db.query('INSERT INTO users (name) VALUES (?)', ('Alice',))
    db.query('INSERT INTO users (name) VALUES (?)', ('Bob',))

    db.query('SELECT * FROM users')
    users = db.fetchall()

    return jsonify(users)

@app.teardown_appcontext
def teardown_db(exception):
    """Cierra la conexión a la base de datos al finalizar la solicitud"""
    db = Database()
    db.close()

if __name__ == '__main__':
    app.run(debug=True)
