import requests
import json
import os

from settings import db


def get_users_tokens(purifier_id):
    tokens = db.users_token.find({"purifier_id": 1})
    tokens = [t["user_token"] for t in tokens]

    return tokens


def send_notification(data):
    msg = None

    if data["battery"] <= 5:
        msg = f"Bateria do purificador está baixa: {data['battery']}%. Recarregue."

    for m in data["mobile_sensors"]:
        if m["battery"] <= 5:
            msg = f"Bateria do Mobile Sensor {m['name']} está baixa: {m['battery']}%. Recarregue."
        if m["quality"] == "bad":
            msg = f"O ambiente {m['name']} precisa ser purificado."


    if data["progress"] == 100 and data["active"]:
        msg = f"Purificação concluída!"

    header = {"Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Basic {os.getenv('ONESIGNAL_USER_TOKEN')}"}

    if msg: 
        payload = {"app_id": os.getenv("ONESIGNAL_TOKEN"),
            "include_player_ids": get_users_tokens(data["_id"]),
            "contents": {"en": msg}}
        req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
        print(f"Sending notification: {msg}")
        print(req.status_code, req.reason)
