from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configure DB connection
db_config = {
    'host': 'mysql_container',   # or container name if using Docker
    'user': 'root',
    'password': 'root@123',
    'database': 'testdb'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    return "2-Tier Flask + MySQL App is running!"

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User added successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
