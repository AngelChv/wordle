from rich import Console


class WordGenerator:
    console = Console()

    def get_random_word(self) -> str:
        """
        Genera una palabra aleatoria.
        :return: palabra aleatoria.
        """