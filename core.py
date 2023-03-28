import json
import datetime as Dt


# узнаем статус ВК и запрашиваем коль-во фото
def get_status_id(dict_id, dict_ph):
    print(f'Фамилия - {dict_id["last_name"]}\n'
          f'Имя - {dict_id["first_name"]}')
    if not dict_id['is_closed']:
        print(f'найдено {dict_ph["response"]["count"]} фотографий')
        count = input('введите количество для выгрузки -')
        return int(count)
    else:
        print('профиль закрыт')
        count = 0
        return count


# Оснавная функция - из полученного ответа vk.get_photos,
def save_photo(dict_ph, dict_id, self):
    count = get_status_id(dict_id, dict_ph)
    if count == 0:
        return print('невозможно выгрузить фото')
    i = 0
    for photo_list in dict_ph['response']['items']:
        top = get_size(photo_list['sizes'])
        for photo in photo_list['sizes'][::-1]:
            if photo['width'] == top[-1] and i != count:
                file_url = photo['url']
                date = photo_list['date']
                file_name = get_name_file(photo_list['likes']['count'], date)
                name_to_json(file_name, photo['type'], date)
                self.get_upload(file_url, file_name)
                i += 1
                break


# получаем список всех доступных размеров для фото
def get_size(list_size):
    dict_size = {}
    for size in list_size:
        dict_size[size['width']] = size['type']
    top = sorted(dict_size)
    return top


# записываем в json с названиями файлов
def name_to_json(name, size, date):
    with open("backup.json", 'r', encoding='utf-8') as f:
        temp = json.load(f)
        list_photo = {}
        list_photo['file name'] = f'{name}.jpg'
        list_photo['size'] = size
        date = Dt.datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        for i in temp:
            if list_photo['file name'] in i.values():
                list_photo['date'] = date
        temp.append(list_photo)
    with open("backup.json", 'w', encoding='utf-8') as f:
        json.dump(temp, f)


# Задаем имя файла, если повторяется, добавляем дату
def get_name_file(name, date):
    name = f'likes-{name}'
    date = Dt.datetime.fromtimestamp(date).strftime('%Y-%m-%d')
    with open("backup.json", 'r') as f:
        name_file = json.load(f)
        for name_ in name_file:
            if f'{name}.jpg' == name_['file name']:
                name = f'{name}-{date}'
                return name
        else:
            return name


# Cоздаем файл json
def create_buckup_list():
    with open("backup.json", 'w', encoding='utf-8') as f:
        temp = [{'file name': 'name'}]
        json.dump(temp, f)
