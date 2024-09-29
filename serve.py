import flask
import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime

app = flask.Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'python',
    'password': 'password!',
    'database': 'rsvp',
    'ssl_disabled': True
}

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

@app.route('/')
def rsvp_form():
    return flask.render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets'), 'favicon.ico')
@app.route('/bg.jpeg')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'assets'), 'bg.jpeg')


@app.route('/submit', methods=['PUT'])
def put_data():
    if not flask.request.is_json:
        return "Request must be JSON", 400
    
    data = flask.request.get_json()

    name = data.get('name')
    coming = data.get('coming')
    ip = flask.request.remote_addr
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not name:
        return "Missing required data", 400

    connection = create_connection()
    cursor = connection.cursor()
    
    try:
        query = "INSERT INTO rsvp (name, coming, ip, date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, coming, ip, date))
        connection.commit()
        return "Success", 201
    except Error as e:
        print(f"Error: {e}")
        return "Failed to insert data", 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
