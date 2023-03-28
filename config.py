import os
from dotenv import load_dotenv


# Подгружаем из переменных окружения, локально будут храниться токены в файл .env
load_dotenv()
token_vk = os.getenv('token_vk')
token_ya = os.getenv('token_ya')
