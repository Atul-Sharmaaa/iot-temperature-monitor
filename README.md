Execution:
1. Publisher Program:
-Simulates temperature readings and publishes them to an MQTT broker.
-The program will publish a new temperature reading every 60 seconds.

2. Subscriber Program:
-Subscribes to the MQTT topic to receive temperature data, checks for threshold breaches, and logs the data locally.
-The program will raise an alarm if the temperature exceeds the threshold for 5 consecutive readings (5 minutes).

3. Server Program:
-Exposes the latest temperature data via an HTTP API.
-Access the latest temperature reading by making a GET request to: "http://localhost:5000/temperature"
-In our local we access this temperature data "http://127.0.0.1:5000/temperature"

4.Requirements
-Python 3.x
-paho-mqtt
-flask
