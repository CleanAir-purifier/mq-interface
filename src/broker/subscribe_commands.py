import random
import datetime
import os
import json
from paho.mqtt import client as mqtt_client

from settings import db

broker = 'baboon.rmq.cloudamqp.com'
port = 1883
topic = "commands.*"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = os.getenv("BROKER_USER", "username")
password = os.getenv("BROKER_PASSWORD", "password")


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data = json.loads(msg.payload)

        if msg.topic == "commands/purifier":
            db.clean_air.update_one(
                {"_id": 1}, {"$set": {"active": data["active"]}},
                upsert=True
            )
            print("Device Updated")
        
        elif msg.topic == "commands/mobile_sensors":
            purifier = db.clean_air.find_one({"mobile_sensors.id": data["id"]})
            updated = purifier["mobile_sensors"]
            for e in updated:
                if e["id"] == data["id"]:
                    e["active"] = data["active"]

            purifier["mobile_sensors"] = updated

            mobile_sensor_data = db.clean_air.update_one(
                {"mobile_sensors.id":data["id"]}, {"$set": purifier}
            )
            print("Device Updated")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
