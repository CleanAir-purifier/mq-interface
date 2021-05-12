import json

from broker.publish import run

data = {
    "device": {
        "type": "purifier",
        "battery": 50,
        "filter_status": "medium",
        "light_status": "good",
        "active": False,
        "id": 1,
        "progress": 50,
        "mobile_sensors": [
            {
                "name": "",
                "type": "mobile_sensor",
                "battery": 80,
                "quality": "good",
                "active": True,
                "id": 1,
                "metrics": {
                    "MP": "15",
                    "O2": "25",
                    "CO": "2",
                    "NO2": "45",
                    "SO2": "5"
                },
                "temperature": "23",
                "humidity": "54"
            },
            {
                "name": "",
                "type": "mobile_sensor",
                "battery": 20,
                "quality": "bad",
                "active": False,
                "id": 2,
                "metrics": {
                    "MP10": "15",
                    "MP25": "8",
                    "O2": "25",
                    "CO2": "2",
                    "NO2": "45",
                    "SO2": "5"
                },
                "temperature": "23",
                "humidity": "53"
            }
        ]
    }
}

run("data.purifier", json.dumps(data))
