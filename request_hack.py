import requests
from dotenv import dotenv_values


class RequestHack:

    url = dotenv_values('.env').get('APP_URL')
    token = dotenv_values('.env').get('TOKEN')

    def post(self, params): 
        header = {'X-Auth-Token': self.token}
        return requests.post(f'{self.url}/play/magcarp/player/move',data=params, headers=header).json()
    def get(self):
        return requests.get(f'{self.url}/rounds/magcarp').json()
