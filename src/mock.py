import json

from broker.publish import run

data = {
        "_id": 1,
        "type": "purifier",
        "battery": 5,
        "filter_status": "medium",
        "light_status": "good",
        "active": False,
        "progress": 50,
        "mobile_sensors": [
            {
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
                "type": "mobile_sensor",
                "battery": 20,
                "quality": "bad",
                "active": False,
                "id": 2,
                "metrics": {
                    "MP": "15",
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

run("data.purifier", json.dumps(data))
