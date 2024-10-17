import random

import wordfreq

from resource_manager import get_resource, set_words
from word_generator import WordGenerator


class WordFreq(WordGenerator):
    def __init__(self, word_length: int = 5):
        self.word_length: int = word_length
        self.resource_path: str = "wordfreq.json"
        self.words: list[str] = get_resource(self.resource_path)


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
            filtered_words: list[str] = [p.lower() for p in words if len(p) == self.word_length]
            set_words(filtered_words, self.resource_path)
            rand_word = random.choice(filtered_words)

        return rand_word