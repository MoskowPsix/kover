import requests
from dotenv import dotenv_values


class RequestHack:

    url = dotenv_values('.env').get('APP_URL')
    token = dotenv_values('.env').get('TOKEN')

    def post(self, params: object): 
        return requests.post(f'{self.url}/play/magcarp/player/move', params, headers=f'X-Auth-Token={self.token}').json
    def get(self):
        return requests.get(f'{self.url}/rounds/magcarp').json()
