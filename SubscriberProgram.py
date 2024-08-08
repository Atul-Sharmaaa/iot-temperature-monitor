import time
import sqlite3
from paho.mqtt.client import Client

BROKER = 'broker.hivemq.com'
PORT = 1883
TOPIC = 'hotel/branch/temperature'
THRESHOLD = 25.0  # Temperature threshold
ALARM_THRESHOLD = 5  # Number of consecutive readings
DATABASE = 'sensor_data.db'

consecutive_count = 0

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS temperature_data 
                 (timestamp TEXT, temperature REAL)''')
    conn.commit()
    conn.close()

# Save temperature data to the database
def save_temperature(timestamp, temperature):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (?, ?)", (timestamp, temperature))
    conn.commit()
    conn.close()

def on_message(client, userdata, message):
    global consecutive_count
    temperature = float(message.payload.decode())
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    save_temperature(timestamp, temperature)

    if temperature > THRESHOLD:
        consecutive_count += 1
        if consecutive_count >= ALARM_THRESHOLD:
            print(f'Alarm! Temperature exceeded {THRESHOLD}°C for {ALARM_THRESHOLD} consecutive readings.')
    else:
        consecutive_count = 0

def subscribe_temperature():
    client = Client()
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
    client.loop_forever()

if __name__ == '__main__':
    init_db()
    subscribe_temperature()