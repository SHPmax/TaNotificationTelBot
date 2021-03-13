import requests
import random
from init import *


try:
    with open(TENOR_API_KEY_PATH, 'r') as file:
        tenor_api_token = file.read().splitlines()[0]
except Exception as e:
    logging.error(e)

TENOR_API_URL = 'https://g.tenor.com/v1/random?locale=ru_RU&q=%s&limit=1&key=%s'

SEARCH_KEYS = [
    'funny', 'food', 'Trending', 'spring_forward', 'cool', 'pain', 'math', 'life', 'stop', 'university',
    'боль', 'почему', 'dsaddas', 'математика', 'тупой', 'why'
]


def get_random_gif_url():
    request_url = TENOR_API_URL % (random.choice(SEARCH_KEYS), tenor_api_token)
    logging.error(request_url)
    try:
        response = requests.get(request_url)
        pay_load = response.json()
        gif_url = pay_load['results'][0]['media'][0]['mediumgif']['url']
    except:
        return None
    return gif_url
