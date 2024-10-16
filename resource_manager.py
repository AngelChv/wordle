import json
import os
from json import JSONDecodeError


def get_resource(name: str) -> list[str]:
    """
    Función para obtener una lista de palabras de un recurso local.
    :return: Lista de palabras.
    """
    try:
        with open("resources/" + name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"El archivo {name} no fue encontrado.")
        return []
    except JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {name}.")
        return []
    except OSError as e:
        print(f"Error de entrada/salida: {e}")
        return []


def set_words(words: list[str], name: str) -> None:
    """
    Almacena una lista de palabras en formato json.
    :param name: Nombre del recurso.
    :param words: Lista de palabras.
    :return: :class:`None <None>`
    """
    if not os.path.exists('resources'):
        os.mkdir("resources")

    try:
        with open('resources/' + name, 'wt', encoding='utf-8') as f:
            json.dump(words, f)
    except OSError as e:
        print(f"No se han podido guardar las palabras: {e}")
