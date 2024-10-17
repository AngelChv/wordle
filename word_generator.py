from rich.console import Console


class WordGenerator:
    console = Console()

    def get_rand_word(self) -> str:
        """
        Genera una palabra aleatoria.
        :return: palabra aleatoria.
        """