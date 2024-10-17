from char import Char


class Word:
    """
    Almacena una lista de objetos :class:`Char` con el estado de cada letra.
    Si alguna letra coincide con otra de la palabra oculta y está en la misma posición, obtendrá el color verde.
    Si alguna letra coincide, pero no la posición, será de color amarillo.
    Si no se encuentra en la palabra, será de color gris.
    """
    def __init__(self, word: str):
        """
        :param word: palabra que va a ser transformada en una lista de caracteres con estado.
        """
        self._characters: list[Char] = [Char(c) for c in word.lower()]
        """
        Lista de caracteres creada a partir de la palabra introducida por el usuario, es privada.
        """

    def check(self, hidden_word: str) -> bool:
        """
        Comprueba cada uno de los caracteres de la palabra introducida por el usuario con la palabra oculta y les
        aplica el estado correspondiente.
        :param hidden_word: Palabra oculta a comparar.
        :return: True si se ha acertado la palabra y False en caso contrario.
        """
        # Guarda las posiciones de los caracteres verdes, para que al comprobar los amarillos no se sobreescriban.
        green_positions = set()
        # Guarda los caracteres que no son verdes para evitar contar como amarillos caracteres que ya se marcan como verdes.
        no_green_characters = list(hidden_word)

        # Comprobar caracteres verdes:
        for i, c in enumerate(self.characters):
            if c.char == hidden_word[i]: # Coincide la letra y la posición.
                # Se establece la letra en nulo, para que después no se busque en la comprobación de letras amarillas.
                # Si no se hiciera de esta forma, se detectarían letrás amarillas cuando ya no lo deberían ser,
                # porque ya hay una letra verde indicándolo.
                no_green_characters[i] = None
                # Se añade a las posiciones verdes
                green_positions.add(i)
                c.color = "[green]" # establecer color.

        # Si la cantidad de caracteres verdes es igual al número de caracteres de la palabra,
        # quiere decir que todos los caracteres se han marcado como verde y, por lo tanto, se ha acertado la palabra.
        if len(green_positions) == len(hidden_word): return True

        # Comprobar caracteres amarillos:
        for i, c in enumerate(self.characters):
            # Si es una letra de la palabra sin contar las verdes, se declara como amarilla.
            if i not in green_positions and c.char in no_green_characters:
                c.color = "[yellow]" # establecer color

        return False

    @property
    def characters(self) -> list[Char]:
        """
        Forma de acceder a la lista de caracteres. Similar a un getter.
        :return: lista de caracteres.
        """
        return self._characters

    def get_characters(self) -> list[str]:
        """
        :return: lista de strings con cada letra y su color correspondiente.
        """
        return [c.__str__() for c in self.characters]
