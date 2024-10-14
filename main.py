import json
import os
import random
from json import JSONDecodeError

import requests
from requests import Response, RequestException


def get_resource() -> list[str]:
    """
    Función para obtener una lista de palabras de un recurso local.
    :return: Lista de palabras.
    """
    try:
        with open('resources/words.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("El archivo 'words.json' no fue encontrado.")
        return []
    except JSONDecodeError:
        print("Error al decodificar el archivo JSON.")
        return []
    except OSError as e:
        print(f"Error de entrada/salida: {e}")
        return []


def get_request() -> Response:
    """
    Realiza una petición a la API datamuse para obtener una serie de palabras con 5 letras en español.
    :return: :class:`Response <Response>` que almacena el código de estado y el contenido de la petición.
    """
    # Utilizo la api datamuse para obtener palabras.
    url: str = 'https://api.datamuse.com/words'
    # parámetros que definen la cantidad de palabras y la condición.
    params: dict[str, str | int] = {
        'sp': '?????',
        'max': 1000,
        'v': 'es'
    }
    try:
        # realizo la petición:
        return requests.get(url, params=params)
    except RequestException as e:
        print(f"Error en la petición a la API: {e}")

        # Devolver una respuesta vacía para que se detecte como error.
        return Response()


def set_words(words: list[str]) -> None:
    """
    Almacena una lista de palabras en formato json.
    :param words: Lista de palabras.
    :return: :class:`None <None>`
    """
    if not os.path.exists('resources'):
        os.mkdir("resources")

    try:
        with open('resources/words.json', 'wt', encoding='utf-8') as f:
            json.dump(words, f)
    except OSError as e:
        print(f"No se han podido guardar las palabras: {e}")


def get_rand_word() -> str:
    """
    Genera una palabra aleatoria en función a una lista obtenida de la api datamuse mediante una petición o de un
    archivo local.
    :return: Palabra aleatoria.
    """
    words: list[str] = get_resource()
    rand_word: str
    if words:
        print("Palabras cargadas del fichero local.")
        rand_word = random.choice(words)
    else:
        print("Recurso de palabras no encontrado. Descargándose...")
        response: Response = get_request()
        # Compruebo el estado de la petición (200 es correcta).
        if response.status_code == 200:
            words = [w['word'] for w in response.json()]
            if words:  # compruebo si la respuesta no es nula.
                set_words(words)
                rand_word = random.choice(words)
            else:
                print("Error no se han descargado palabras.")
                rand_word = f"Error, no se han descargado palabras."
        else:
            rand_word = f"Error al conectarse a la API: {response.status_code}"
    return rand_word


if __name__ == '__main__':
    word = get_rand_word()
    print(word)
