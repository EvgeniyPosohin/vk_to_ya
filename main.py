import core
import vk
import ya
import config


if __name__ == '__main__':
    core.create_buckup_list()
    user_id = input('введите ИД пользователя: ')
    vk = vk.VK(config.token_vk, user_id)
    ya_up = ya.YandexD(config.token_ya)
    core.save_photo(vk.get_photos(), vk.users_info(), ya_up)