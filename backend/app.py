# importar flask

from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app) # Permite que React llame sin bloqueos

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='activos',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    
@app.route('/activos')
def get_activos():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM activos")
        rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)