import requests


class YandexD:

    def __init__(self, token: str, folder: str):
        self.token = token
        self.folder = folder


    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}

    def create_folder(self):
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": self.folder, "url": link_url}
        response = requests.put(link_url, headers=headers, params=params)
        return response

    def get_upload(self, file_url, file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        self.create_folder()
        params = {"path": f'{self.folder}/{file_name}', "url": file_url}
        response = requests.post(upload_url, headers=headers, params=params)
        if response.status_code == 202:
            print(f'загружен файл с названием - {file_name}')
        else:
            print(f'файл не загружен - статус {response.status_code}\n'
                  f'{response.json()["message"]}')
