import requests
import random

try:
    with open('config/tenor_gif_api.key', 'r') as file:
        tenor_api_token = file.readline()
except Exception as e:
    logging.error(e)

TENOR_API_URL = 'https://g.tenor.com/v1/random?locale=ru_RU&q=%s&limit=1&key=%s'

SEARCH_KEYS = [
    'funny', 'food', 'Trending', 'spring forward', 'cool', 'pain', 'math', 'life', 'stop', 'university',
    'go go', 'боль', 'почему', 'спасите', 'меня держат', 'в заложниках', 'математика', 'тупой',
    'как поянть, что я тупой', 'алгоритмы'
]


def get_random_gif_url():
    try:
        response = requests.get(
            TENOR_API_URL % (random.choice(SEARCH_KEYS), tenor_api_token)
        )
        pay_load = response.json()
        gif_url = pay_load['results'][0]['media'][0]['mediumgif']['url']
    except:
        return None
    return gif_url
