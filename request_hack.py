import requests
from dotenv import dotenv_values


class RequestHack:

    url = dotenv_values('APP_URL')

    def post(self, params: object): 
        return requests.post(f'{self.url}/play/magcarp/player/move', params)
    def get(self):
        return requests.get(f'{self.url}/rounds/magcarp')
