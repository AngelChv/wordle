class Word:
    """
    Almacena el estado de cada uno de los caracteres de la palabra.
    Si el carácter coincide en la misma posición que el de la palabra a adivinar, se mostrará en verde.
    Si no coincide la posición, pero sí aparece en la palabra, se mostrará en amarillo.
    Pero si no aparece, se mostrará en gris.
    """
    def __init__(self, word: str):
        self.characters: list[str] = list(word)

    def check(self, word: str) -> bool:
        win = True
        for i, c in enumerate(self.characters):
            positions = [index for index, char in enumerate(word) if c == char]
            if positions:
                if i in positions:
                    self.characters[i] = f"[guess]{c}[/]"
                else:
                    win = False
                    self.characters[i] = f"[match]{c}[/]"
            else:
                win = False
                self.characters[i] = f"[none]{c}[/]"
        return win


    def get_characters(self) -> list[str]:
        return self.characters

