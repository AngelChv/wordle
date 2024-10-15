class Word:
    def __init__(self, word: str):
        self.characters: list[str] = list(word)

    def check(self, word: str) -> None:
        for i, c in enumerate(self.characters):
            pos = word.find(c)
            if pos == -1:
                self.characters[i] = f"[grey]{c}[/grey]"
            elif pos == i:
                self.characters[i] = f"[green]{c}[/green]"
            else:
                self.characters[i] = f"[yellow]{c}[/yellow]"


    def get_characters(self) -> list[str]:
        return self.characters

