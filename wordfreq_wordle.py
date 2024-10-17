import random

import wordfreq

from resource_manager import get_resource, set_words
from word_generator import WordGenerator


class WordFreq(WordGenerator):
    # todo pedir recurso.
    def __init__(self):
        self.words: list[str] = get_resource("wordfreq.json")

    def get_rand_word(self) -> str:
        """
        Genera una palabra aleatoria en función a una lista obtenida de la librería wordfreq.
        :return: Palabra aleatoria.
        """
        rand_word: str
        if self.words:
            self.console.print("Palabras cargadas del fichero local (wordfreq.json).")
            rand_word = random.choice(self.words)
        else:
            self.console.print("Recurso de palabras wordfreq no encontrado. Generando...")
            words = wordfreq.top_n_list('es', 1000) # Obtener las 1000 palabras más comunes.
            filtered_words: list[str] = [p for p in words if len(p) == 5]
            set_words(filtered_words, "wordfreq.json")
            rand_word = random.choice(filtered_words)

        return rand_word