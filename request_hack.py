import requests
from dotenv import dotenv_values


class RequestHack:

    url = dotenv_values('.env').get('APP_URL')

    def post(self, params: object): 
        return requests.post(f'{self.url}/play/magcarp/player/move', params).json
    def get(self):
        return requests.get(f'{self.url}/rounds/magcarp').json()
