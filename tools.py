import dotenv
import os


def get_variables() -> tuple:
    dotenv.load_dotenv()
    return os.getenv('YANDEX_WEATHER_API_KEY'), os.getenv('YANDEX_WEATHER_URL')
