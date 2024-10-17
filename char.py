class Char:
    """
    Almacena la letra y su color.
    """
    def __init__(self, char: chr, color: str = "[dim]"):
        # Para identificar atributos privados utilizo la convención de nombrarlos con un "_" delante.
        self._char: chr = char
        self._color: str = color

    # Implementación similar a los getter y setter de java:
    @property
    def char(self) -> chr:
        """
        Similar a un getter.
        :return: un caracter.
        """
        return self._char

    @property
    def color(self) -> str:
        """
        Similar a un getter.
        :return: el color del caracter.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Similar a un setter.
        :param value: valor a aplicar.
        :return: None
        """
        self._color = value

    def __str__(self) -> str:
        """
        :return: cadena con la información de la clase (caracter y color).
        """
        return f"{self.color}{self.char}"
