import paho.mqtt.client as mqtt
import json

HOST = "iot.eclipse.org"	# Default
URL_TOPIC = "sensor/data/sensors_data"       # send messages to this topic
PORT = 1883

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(URL_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    from .models import SensorValues
    data = json.loads(msg.payload)
    print(data)   
    SensorValues.objects.create(raining=data.get('raining'), temperature=data.get('temperature'), humidity=data.get('humidity'))
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(HOST, PORT, 60)
