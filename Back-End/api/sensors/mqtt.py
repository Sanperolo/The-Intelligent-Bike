import paho.mqtt.client as mqtt

HOST = "iot.eclipse.org"	# Default
URL_TOPIC = "sensor/data/"       # send messages to this topic
SENSOR_TOPICS = ['rain', 'humidity', 'temperature']
PORT = 1883

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    for sensor_topic in SENSOR_TOPICS:
        client.subscribe(URL_TOPIC + sensor_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(f'{msg.topic} - {msg.payload}')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, PORT, 60)
