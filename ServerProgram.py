from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'sensor_data.db'

def get_last_temperature():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM temperature_data ORDER BY timestamp DESC LIMIT 1')
    result = c.fetchone()
    conn.close()
    return result

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Sensor Data API!"

@app.route('/sensor/temperature', methods=['GET'])
def last_temperature():
    result = get_last_temperature()
    if result:
        return jsonify({'timestamp': result[0], 'temperature': result[1]})
    else:
        return jsonify({'error': 'No data available'}), 404

if __name__ == '__main__':
    app.run(debug=True)
