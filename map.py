import matplotlib.pyplot as plt
import requests


AREA_SIZE = 9000
URL = " https://games-test.datsteam.dev"

def get_map():
    data = requests.post(URL + "/play/magcarp/player/move", {"transports": []}, headers={"X-Auth-Token": "6703e10e0883d6703e10e08840"}).json()
    return data

def get_anomalies(data):
       anomalies = data['anomalies']
       print(anomalies)

data = get_map()

get_anomalies(data)