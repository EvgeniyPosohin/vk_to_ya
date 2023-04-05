import requests


class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        keys = response.json().keys()
        if 'error' in keys:
            print(f'{response.json()["error"]["error_msg"]}')
        elif 'response' in keys and not response.json()['response']:
            print(f'пользователь с ИД = {self.id} не найден')
        else:
            info = response.json()['response'][0]
            self.id = info['id']
            return info

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'extended': 1, 'album_id': 'profile'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

