from abc import ABC, abstractmethod
from rich.console import Console


class WordGenerator(ABC):
    """
    Clase abstracta padre de otras dos clases, las cuales generan una palabra aleatoria, cada una de una forma distinta.
    :class:`WordFreq`
    :class:`DataMuse`
    """
    console = Console()
    """
    Crear un objeto Console de la librería rich para mostrar tablas y colores.
    """

    @abstractmethod
    def get_rand_word(self) -> str:
        """
        Genera una palabra aleatoria.
        :return: palabra aleatoria.
        """