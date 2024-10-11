import matplotlib.pyplot as plt
import requests
import time
from request_hack import RequestHack


AREA_SIZE = 9000
URL = " https://games-test.datsteam.dev"
fig, ax = plt.subplots()


req_hack = RequestHack()


def get_map():
    data = req_hack.post(params={"transports": []})
    return data


def get_anomalies(data):

    anomalies = data["anomalies"]
    for obj in anomalies:
        circle = plt.Circle(
            (obj["x"], obj["y"]), obj["radius"], color="blue", fill=True, alpha=0.5
        )
        ax.add_artist(circle)


def get_our_kovrs(data):
    kovrs = data["transports"]
    for obj in kovrs:
        circle = plt.Circle((obj["x"], obj["y"]), 50, color="red", fill=True, alpha=0.5)
        ax.add_artist(circle)


def get_enemies(data):
    enemies = data["enemies"]
    for obj in enemies:
        circle = plt.Circle(
            (obj["x"], obj["y"]), 50, color="black", fill=True, alpha=0.5
        )
        ax.add_artist(circle)


while True:
    ax.cla()

    # Задаем размеры области
    ax.set_xlim(0, AREA_SIZE)
    ax.set_ylim(0, AREA_SIZE)

    data = get_map()
    get_anomalies(data)
    get_our_kovrs(data)
    get_enemies(data)

    plt.xlabel("X")
    plt.ylabel("Y")

    # Сохраняем соотношение сторон
    ax.set_aspect("equal", adjustable="box")

    # Показываем график
    plt.savefig("out.png")
    time.sleep(1)
