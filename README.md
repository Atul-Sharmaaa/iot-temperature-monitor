# IoT Temperature Monitor
## Overview
This project simulates an IoT temperature monitoring system. It includes:
- **Publisher Program**: Reads temperature data and publishes it to an MQTT broker.
- **Subscriber Program**: Subscribes to the MQTT topic, checks for threshold breaches, and logs data locally.
- **Server Program**: Exposes the latest sensor data via an HTTP endpoint.

## Requirements
- Python 3.x
- `paho-mqtt`
- `flask`

Install the required Python packages using:
```bash
pip install -r requirements.txt
