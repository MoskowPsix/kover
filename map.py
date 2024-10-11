import matplotlib.pyplot as plt
import requests
import time
from request_hack import RequestHack


AREA_SIZE = 9000
URL = " https://games-test.datsteam.dev"
fig, ax = plt.subplots()


req_hack = RequestHack()
response = []
def get_map(data):
    if (data):
        for kover in data['transports']:
            if kover['x'] >= 8500:
                x = -10
            elif kover['x'] <= 500:
                x = 10  

            if kover['y'] >= 8500:
                y = -10
            elif kover['y'] <= 500:
                y = 10 
            response.append({
                'id': kover['id'],
                "activateShield": False,
                'acceleration': {
                    'x': x,
                    'y': y
                },
                'attack': {
                    'x': 10,
                    'y': 10
                }
            })
        

    data = req_hack.post()
    print(data)
    return data


def get_anomalies(data):

    anomalies = data["anomalies"]
    for obj in anomalies:
        circle = plt.Circle(
            (obj["x"], obj["y"]), obj["radius"]*20, color="blue", fill=True, alpha=0.4
        )
        ax.add_artist(circle)


def get_our_kovrs(data):
    kovrs = data["transports"]
    for obj in kovrs:
        circle = plt.Circle((obj["x"], obj["y"]), 50, color="red", fill=True, alpha=1)
        ax.add_artist(circle)


def get_enemies(data):
    enemies = data["enemies"]
    for obj in enemies:
        circle = plt.Circle((obj["x"], obj["y"]), 50, color="black", fill=True, alpha=1)
        ax.add_artist(circle)

def get_bound(data):
    bound = data["bounties"]
    for obj in bound:
        circle = plt.Circle((obj["x"], obj["y"]), 50, color="yellow", fill=True, alpha=1)
        ax.add_artist(circle)




while True:
    ax.cla()
    data = []
    # Задаем размеры области
    ax.set_xlim(0, AREA_SIZE)
    ax.set_ylim(0, AREA_SIZE)

    data = get_map(data)
    get_anomalies(data)
    get_our_kovrs(data)
    get_enemies(data)
    get_bound(data)

    plt.xlabel("X")
    plt.ylabel("Y")

    # Сохраняем соотношение сторон
    ax.set_aspect("equal", adjustable="box")

    # Показываем график
    plt.savefig("out.png")
    time.sleep(0.5)
