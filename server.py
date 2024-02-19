import requests
from datetime import datetime
from flask import Flask, jsonify
from tools import get_variables

YANDEX_WEATHER_API_KEY, YANDEX_WEATHER_URL = get_variables()

app = Flask(__name__)


@app.route('/weather')
def get_weather():
    # Параметры запроса
    params = {
        'lat': 55.75396,  # Широта для Москвы
        'lon': 37.620393,  # Долгота для Москвы
        'extra': True,
    }
    headers = {
        'X-Yandex-API-Key': YANDEX_WEATHER_API_KEY,
    }

    # Делаем запрос к API Яндекс.Погоды
    response = requests.get(YANDEX_WEATHER_URL, params=params, headers=headers)

    # Проверяем, успешно ли выполнен запрос
    if response.status_code == 200:
        weather_data = response.json()

        # Определяем текущую часть суток
        current_hour = datetime.now().hour
        if 6 <= current_hour < 12:
            next_part_of_day = 'day'
        elif 12 <= current_hour < 18:
            next_part_of_day = 'evening'
        elif 18 <= current_hour < 24:
            next_part_of_day = 'night'
        else:
            next_part_of_day = 'morning'

        # Получаем прогноз на следующую часть суток
        next_part_of_day_forecast \
            = weather_data['forecasts'][0]['parts'][next_part_of_day]
        return jsonify(next_part_of_day_forecast)
    else:
        return jsonify({'error': 'Failed to get weather data'}), 500


if __name__ == '__main__':
    app.run(debug=True)
