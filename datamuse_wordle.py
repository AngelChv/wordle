import random
import re
import requests
from pygments.lexer import words
from regex import Pattern
from requests import Response, RequestException
from rich.console import Console

from resource_manager import get_resource, set_words
from word_generator import WordGenerator

console = Console()

class DataMuse(WordGenerator):
    def __init__(self):
        # todo pedir recurso.
        self.words: list[str] = get_resource("datamuse.json")

    def get_rand_word(self) -> str:
        """
        Genera una palabra aleatoria en función a una lista obtenida de la api datamuse mediante una petición o de un
        archivo local.
        :return: Palabra aleatoria.
        """
        rand_word: str
        if self.words:
            console.print("Palabras cargadas del fichero local (datamuse.json).")
            rand_word = random.choice(self.words)
        else:
            console.log("Descárgando...")
            response: Response = self.get_request()
            # Compruebo el estado de la petición (200 es correcta).
            if response.status_code == 200:
                words = [w['word'] for w in response.json()]
                if words:  # compruebo si la respuesta no es nula.
                    filtered_words = self.filter_words(words)
                    set_words(filtered_words, "datamuse.json")
                    rand_word = random.choice(filtered_words)
                else:
                    console.print("Error no se han descargado palabras.", style="red")
                    rand_word = f"Error, no se han descargado palabras."
            else:
                rand_word = f"Error al conectarse a la API: {response.status_code}"
        return rand_word


    def get_request(self) -> Response:
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
            console.print(f"Error en la petición a la API: {e}", style="red")
            # Devolver una respuesta vacía para que se detecte como error.
            return Response()


    def filter_words(words: list[str]) -> list[str]:
        word_length: int = 5
        regex: Pattern = re.compile(fr"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{{{word_length}}}$")
        return [word for word in words if regex.match(word)]
