# importar flask

from flask import Flask, jsonify,request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app) # Permite que React llame sin bloqueos

""" Conexion a la base de datos  """
def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='activos',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
""" ---------------------- """
    
    
# OBTENER ACTIVOS GET
@app.route('/activos')
def get_activos():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM activos")
        rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

""" ----------------- """

# Crear activos con método POST 

@app.route('/activos', methods=['POST'])
def crear_activo():
    data = request.get_json()
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = "INSERT INTO activos (nombreActivo, ubicacion, estado) VALUES (%s, %s, %s)"
        cursor.execute(sql, (data['nombreActivo'], data['ubicacion'], data['estado']))
        conn.commit()
    conn.close()
    return jsonify({'msg': 'Creado'}), 201




if __name__ == '__main__':
    app.run(debug=True)