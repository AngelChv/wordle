class Word:
    def __init__(self, word: str):
        self.characters: list[str] = list(word)
        # todo pedir colores al inicializar

    def check(self, word: str) -> bool:
        win = True
        for i, c in enumerate(self.characters):
            positions = [index for index, char in enumerate(word) if c == char]
            if positions:
                if i in positions:
                    self.characters[i] = f"[green]{c}[/green]"
                else:
                    win = False
                    self.characters[i] = f"[yellow]{c}[/yellow]"
            else:
                win = False
                self.characters[i] = f"[grey]{c}[/grey]"
        return win


    def get_characters(self) -> list[str]:
        return self.characters

