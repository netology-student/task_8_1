import requests

class SuperHeroInfo:
    def __init__(self, token):
        self.token = token

    def id_by_name(self, name: str):
        id = ''
        url = f'https://superheroapi.com/api/{self.token}/search/{name}'
        resp = requests.get(url)
        if resp.status_code != 200:
            print(resp.text)
        else:
            resp_json = resp.json()
            if resp_json['response'] != 'success':
                print(f'{resp_json["response"]}: {resp_json["error"]}')
            else:
                id = resp_json['results'][0]['id']

        return id

    def get_intelligence(self, name: str):
        result = 0
        id = self.id_by_name(name);
        if id != '':
            url = f'https://superheroapi.com/api/{self.token}/{id}/powerstats'
            resp = requests.get(url)
            if resp.status_code != 200:
                print(resp.text)
            else:
                resp_json = resp.json()
                if resp_json['response'] != 'success':
                    print(f'{resp_json["response"]}: {resp_json["error"]}')
                else:
                    result = int(resp.json()['intelligence'])

        return result