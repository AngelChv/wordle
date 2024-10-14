import random
import requests

def get_rand_word() -> list[str]:
    # Utilizo la api datamuse para obtener palabras.
    url = 'https://api.datamuse.com/words'
    # parámetos que definen la cantidad de palabras, el idioma y la condición.
    params = {
        'sp': '?????',
        'max': 1000,
        'v': 'es'
    }
    # realizo la petición:
    response = requests.get(url, params=params)

    # Compruebo el estado de la petición (200 es correcta).
    if response.status_code == 200:
        # Obtener palabras:
        word_list = [word['word'] for word in response.json()]

        return word_list
    else:
        print("Error al conectarse a la API: ", response.status_code)

words = get_rand_word()
if words:
    print(words)
else: print('No se encuentran palabras.')