from aiogram import Dispatcher
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'AvaProDetailing_Bot'
    database_url: str
    role_list: str = '{1:"client",2:"administrator",3:"superuser"}'
    default_role: int = 1

    min_fio_len: int = 2
    max_fio_len: int = 100
    fio_alphabet_error: str = 'Поле содержит недопустимые символ'
    min_age: int = 5844
    max_age: int = 40178
    age_error: str = 'Ваш возраст не соответствует допустимому'
    max_phone_len: int = 15
    phone_error: str = 'invalid phone number format'

    min_name_len: int = 1
    max_name_len: int = 50
    min_address_len: int = 1
    max_address_len: int = 250
    min_description_len = 1
    name_error: str = 'Имя не может быть пустым!'
    address_error: str = 'Адрес автомойки не может быть пустым!'

    dp: Dispatcher = Dispatcher()
    bot_drop_pending_updates: bool = 1
    bot_request_timeout: int = 30
    bot_parse_mode: str = 'html'
    telegram_bot_token: str = '123456789'
    telegram_webapp_url: str = 'https://ya.ru'
    host_ip: str = '0.0.0.0'
    host_url: str = 'https://example.com'
    app_port: int = 443  # Из энва ест в виде стринга, переконвертирую в мейне

    class Config:
        env_file = '.env'


settings = Settings()
