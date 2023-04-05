import core
import vk
import ya
import config


if __name__ == '__main__':
    core.create_buckup_list()
    user_id = input('введите ИД пользователя: ')
    vk = vk.VK(config.token_vk, user_id)
    info = vk.users_info()
    ya_up = ya.YandexD(input('введите токен для Яндекс Диска:'),
    input('укажите название папки для хранения:'))
    core.save_photo(vk.get_photos(), info, ya_up)