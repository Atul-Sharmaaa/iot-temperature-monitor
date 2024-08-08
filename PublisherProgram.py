import time
import random
import paho.mqtt.client as mqtt

BROKER = 'broker.hivemq.com'
PORT = 1883
TOPIC = 'hotel/branch/temperature'
DELAY = 60  # 60 seconds

def simulate_temperature():
    # Simulate temperature between 18°C and 30°C
    return round(random.uniform(18.0, 30.0), 2)

def publish_temperature():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    try:
        while True:
            temperature = simulate_temperature()
            client.publish(TOPIC, temperature)
            print(f'Published temperature: {temperature}°C')
            time.sleep(DELAY)
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()

if __name__ == '__main__':
    publish_temperature()