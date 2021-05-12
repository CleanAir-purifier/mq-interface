import os
import random
import time
from paho.mqtt import client as mqtt_client


broker = 'baboon.rmq.cloudamqp.com'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = os.getenv("BROKER_USER", "username")
password = os.getenv("BROKER_PASSWORD", "password")


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, msg):
    while True:
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send msg to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        time.sleep(3600)


def run(topic, msg):
    client = connect_mqtt()
    client.loop_start()
    publish(client, topic, msg)
