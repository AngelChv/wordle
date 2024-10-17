import re
from typing import Callable, Pattern

from rich.console import Console
from rich.table import Table

from datamuse_wordle import DataMuse
from word import Word
from word_generator import WordGenerator
from wordfreq_wordle import WordFreq

# Crear un objeto Console de la librería rich para mostrar tablas y colores.
console = Console()


def main():
    """
    todo guardar puntuaciones.
    todo mostrar un teclado con las letras que están en la palabra.
    Author: <Ángel Chicote>
    Consejos: ejecutar si no vés los colores la terminal de tu ide, ejecutaló en la terminal directamente.
    Instalaciones:
    ---- Necesaria ----
    pip install rich / python -m install rich
    ---- Wordfreq ----
    pip install wordfreq / python -m install wordfreq
    ---- Data Muse ----
    pip install request / python -m install request
    """
    console.rule("Bienvenido al [bold][red]W[/][green]o[/][yellow]r[/][blue]d[/][magenta]l[/][cyan]e[/][/] para terminal!")

    #Pedir al usuario de qué forma quiere obtener las palabras:
    print("Este programa necesita cargar una lista de palabras, para ello existen dos opciones:")
    print("- Usar data muse (una api que proporciona palabras en inglés y en español) necesita la librería request. "
          "programa funciona en español, pero la api muchas veces confunde palabras en ingles y las introduce en la lista.")
    print("- Wordfreq, es una librería de python que proporciona una serie de palabras comunes, necesita de instalación, "
          "pero proporcióna palabras de uso frecuente más fáciles de adivinar.")
    op = request_int(
        "[blue]1. DataMuse.\n2. Wordfreq.\nElige: ",
        lambda o: True if re.match(f"^[12]$", o) else False
    )

    # En función de la opción elegida, se carga un módulo u otro.
    try:
        match op:
            case 1: word_generator: WordGenerator = DataMuse()
            case 2: word_generator: WordGenerator = WordFreq()
            case _: raise RuntimeError("No se ha elegído una opción válida para el módulo de carga de palabras.")

        # Bucle del juego:
        game_loop(word_generator)
    except ModuleNotFoundError as mnfe:
        console.print("No se ha podido encontrar el módulo que se intenta cargar: ", mnfe, style="red")
    except RuntimeError as rune:
        console.print(rune, style="red")


def game_loop(word_generator: WordGenerator) -> None:
    # Crear una tabla
    table = Table(title="[bold cyan]Wordle[/]", show_header=False, style="magenta")
    # Genéro una palabra aleatória.
    hidden_word: str = word_generator.get_rand_word()
    # Longitud de la palabra.
    word_length: int = len(hidden_word)
    # Patrón que deben cumplir las palabras introducidas.
    regex: Pattern = re.compile(fr"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{{{word_length}}}$")
    win: bool = False  # almacena si el jugador ha ganado.
    turn: int = 1  # turno actual
    attempts: int = 6  # máximo de rondas.

    console.print(f"Tienes [bold]{attempts} turnos[/] para adivinar la palabra oculta.")
    console.print(f"En cada intento deberás proporcionar una palabra de [bold]{word_length} letras[/].")
    console.print("Si una letra está en la misma posición que la palabra oculta, aparecerá en [green]verde[/].")
    console.print("Si una letra está en la palabra, pero no en la misma posición, aparecerá en [yellow]amarillo[/].")
    console.print("Si una letra no está en toda la palabra, aparecerá en [dim]gris[/].")

    # El bucle de juego continúa si no se han acabado las rondas ni el jugador ha ganado.
    while turn <= attempts and not win:
        # Crear objeto Word con la palabra pedida por teclado, la cual se validará con el regex.
        player_word: Word = Word(request_str(f"{turn}: ", lambda word: True if regex.match(word) else False))
        # Comprobar la palabra y establecer los colores de cada carácter.
        win = player_word.check(hidden_word)
        # Añadir filas a la tabla, cada carácter es una columna, por lo tanto, utilizo '*' para separar los elementos
        # de la lista de carácteres en los diferentes argumentos de la función.
        table.add_row(*player_word.characters)
        # Imprimir la tabla
        console.print(table)
        # Incrementar turno
        turn += 1

    if win:  # Victoria.
        console.print("[green]Has ganado![/]")
    else:  # Derrota.
        console.print(f"[red]Has perdido, la palabra era: {hidden_word}[/]")

    if console.input("[underline]Quieres seguir jugando? (s/n): ").strip().lower() == 's': game_loop(word_generator)


def request_str(message: str, validator: Callable[[str], bool]) -> str:
    try:
        string: str = console.input(message).strip().lower()
        if string and validator(string):
            return string
        else:
            console.print("La palabra no es válida.", style="yellow")
            return request_str(message, validator)
    except UnicodeDecodeError as ude:
        console.print("Error: ", ude, style="red")
        return request_str(message, validator)


def request_int(message: str, validator: Callable[[str], bool]) -> int:
    try:
        num: str = console.input(message).strip()
        if num and validator(num):
            return int(num)
        else:
            console.print("El número no es válido.", style="yellow")
            return request_int(message, validator)
    except (UnicodeDecodeError, ValueError, TypeError) as e:
        console.print("Error: ", e, style="red")
        return request_int(message, validator)


if __name__ == '__main__':
    main()