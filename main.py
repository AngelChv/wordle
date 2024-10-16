"""
Todo guardar palabras usadas (en un set si es conveniente o una lista).
todo filtrar palabras.
Instalaciones:
pip install rich
"""
import json
import os
import random
import re
from json import JSONDecodeError
from shutil import which
from typing import Callable, Pattern

import requests
from requests import Response, RequestException
from rich.console import Console
from rich.table import Table
from word import Word


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


def request_str(message: str, validator: Callable[[str], bool]) -> str:
    string: str = input(message).strip().lower()
    if string and validator(string):
        return string
    else:
        print("La palabra no es válida.")
        return request_str(message, validator)

    #return string if string and validator(string) else request_str(message, validator)


def main():
    # Crear un objeto Console
    console = Console()
    # Crear una tabla
    table = Table(title="Wordle", show_header=False)

    win: bool = False
    hidden_word: str = get_rand_word()
    turn: int = 1
    attempts: int = 6
    word_length: int = len(hidden_word) # todo hacer que se pida al usuario.
    regex: Pattern = re.compile(fr"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{{{word_length}}}$")
    words_used: list[Word] = list()

    print("Bienvenido al Wordle para terminal!")
    print("Tienes 5 turnos para adivinar la palabra oculta.")
    print("En cada intento deberás proporcionar una palabra de 5 letras.")
    print("Si una letra está en la misma posición que la palabra oculta, aparecerá en verde.")
    print("Si una letra está en la palabra, pero no en la misma posición, aparecerá en naranja.")
    print("Si una letra no está en toda la palabra, aparecerá en gris.")

    while turn <= attempts and not win:
        player_word: Word = Word(request_str(f"{turn}: ", lambda word: True if regex.match(word) else False))
        words_used.append(player_word)
        win = player_word.check(hidden_word)

        # Añadir filas
        table.add_row(*player_word.characters)

        # Imprimir la tabla
        console.print(table)

        # Incrementar turno
        turn += 1

    if win:
        console.print("[green]Has ganado![/green]")
    else:
        console.print(f"[red]Has perdido, la palabra era: {hidden_word}[/red]")

    if input("Quieres seguir jugando? (s/n): ").strip().lower() == 's': main()


if __name__ == '__main__':
    main()