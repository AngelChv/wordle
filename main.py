import importlib
import re
from typing import Callable, Pattern

from rich.console import Console
from rich.table import Table

from word import Word


def main():
    """
    todo guardar puntuaciones.
    Author: <Ángel Chicote>
    Instalaciones:
    pip install rich
    """
    # Crear un objeto Console de la librería rich para mostrar tablas y colores.
    console = Console()
    console.print("Bienvenido al [red]W[/red][green]o[/green][yellow]r[/yellow][blue]d[/blue][magenta]l[/magenta][cyan]e[/cyan] para terminal!")

    #Pedir al usuario de qué forma quiere obtener las palabras:
    print("Este programa necesita cargar una lista de palabras, para ello existen dos opciones:")
    print("- Usar data muse (una api que proporciona palabras en inglés y en español) no requiere de instalación. "
          "programa funciona en español, pero la api muchas veces confunde palabras en ingles y las introduce en la lista.")
    print("- Wordfreq, es una librería de python que proporciona una serie de palabras comunes, necesita de instalación, "
          "pero proporcióna palabras de uso frecuente más fáciles de adivinar.")
    op = request_int(
        "1. DataMuse.\n2. Wordfreq.\nElige: ",
        lambda o: True if re.match(f"^[12]$", o) else False
    )

    # En función de la opción elegida, se carga un módulo u otro.
    try:
        match op:
            case 1: modulo = importlib.import_module("datamuse_wordle")
            case 2: modulo = importlib.import_module("wordfreq_wordle")
            case _: raise RuntimeError("No se ha elegído una opción válida para el módulo de carga de palabras.")

        # Crear una tabla
        table = Table(title="Wordle", show_header=False)
        # Longitud de la palabra.
        word_length: int = 5
        # Patrón que deben cumplir las palabras introducidas.
        regex: Pattern = re.compile(fr"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{{{word_length}}}$")
        # Genéro una palabra aleatória.
        hidden_word: str = modulo.get_rand_word()
        win: bool = False # almacena si el jugador ha ganado.
        turn: int = 1 # turno actual
        attempts: int = 6 # máximo de rondas.

        print("Tienes 5 turnos para adivinar la palabra oculta.")
        print("En cada intento deberás proporcionar una palabra de 5 letras.")
        print("Si una letra está en la misma posición que la palabra oculta, aparecerá en verde.")
        print("Si una letra está en la palabra, pero no en la misma posición, aparecerá en naranja.")
        print("Si una letra no está en toda la palabra, aparecerá en gris.")

        # El bucle de juego continúa si no se han acabado las rondas ni el jugador ha ganado.
        while turn <= attempts and not win:
            # Crear objeto Word con la palabra pedida por teclado, la cual se validará con el regex.
            player_word: Word = Word(request_str(f"{turn}: ", lambda word: True if regex.match(word) else False))
            #Comprobar la palabra y establecer los colores de cada carácter.
            win = player_word.check(hidden_word)
            # Añadir filas a la tabla, cada carácter es una columna, por lo tanto, utilizo '*' para separar los elementos
            # de la lista de carácteres en los diferentes argumentos de la función.
            table.add_row(*player_word.characters)
            # Imprimir la tabla
            console.print(table)
            # Incrementar turno
            turn += 1

        if win: # Victoria.
            console.print("[green]Has ganado![/green]")
        else: # Derrota.
            console.print(f"[red]Has perdido, la palabra era: {hidden_word}[/red]")

        if input("Quieres seguir jugando? (s/n): ").strip().lower() == 's': main()
    except ModuleNotFoundError as mnfe:
        print("No se ha podido encontrar el módulo que se intenta cargar: ", mnfe)
    except RuntimeError as rune:
        print(rune)




def request_str(message: str, validator: Callable[[str], bool]) -> str:
    try:
        string: str = input(message).strip().lower()
        if string and validator(string):
            return string
        else:
            print("La palabra no es válida.")
            return request_str(message, validator)
    except UnicodeDecodeError as ude:
        print("Error: ", ude)
        return request_str(message, validator)


def request_int(message: str, validator: Callable[[str], bool]) -> int:
    try:
        num: str = input(message).strip()
        if num and validator(num):
            return int(num)
        else:
            print("El número no es válido.")
            return request_int(message, validator)
    except [UnicodeDecodeError, ValueError, TypeError] as e:
        print("Error: ", e)
        return request_int(message, validator)


if __name__ == '__main__':
    main()