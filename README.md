# Wordle para Terminal en Python

## Descripción general del proyecto
Este proyecto recrea el famoso juego de palabras “Wordle” para ejecutarse en la terminal, disponible tanto en español como en inglés. El objetivo es adivinar una palabra oculta con un número limitado de intentos, mostrando pistas visuales sobre los caracteres correctos.

## Objetivos
- Desarrollar una aplicación interactiva en Python.
- Cubrir los siguientes conceptos:
  - Estructuras condicionales
  - Bucles
  - Funciones
  - Funciones lambda
  - Estructuras de datos
  - Librerías
  - Clases
  - Manejo de excepciones
  - Peticiones HTTP (JSON)

## Entorno de trabajo y herramientas
- **Lenguaje de programación**: Python 3.13.0
- **IDE**: PyCharm, por su facilidad y herramientas para el desarrollo de Python.

## Bibliotecas utilizadas
- **Rich**: Para mejorar la visualización en la terminal con colores y tablas.
- **Requests**: Para realizar peticiones HTTP a la API de Datamuse.
- **Wordfreq**: Para obtener un listado de palabras frecuentes en español.

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/AngelChv/wordle
    ```
2. Instalar las dependencias:
    ```bash
    pip install requests wordfreq rich
    ```

## Estructura de la aplicación
- **Main**: Inicializa el juego y selecciona una palabra al azar utilizando la API de Datamuse o Wordfreq. Controla el flujo del juego y la interacción con el usuario.
- **Resource Manager**: Gestiona la obtención y almacenamiento de palabras en un archivo local.
- **Word Generator**: Clase abstracta de la que heredan las clases para obtener palabras de Datamuse o Wordfreq.
- **Char**: Representa un carácter de la palabra, incluyendo su color para la visualización del estado del juego.
- **Word**: Gestiona un conjunto de caracteres y realiza las comprobaciones de aciertos.

## Posibles ampliaciones
- Guardar las mejores puntuaciones locales.
- Mostrar un teclado visual con las letras descubiertas y no probadas.
- Mejorar el apartado gráfico.
- Configurar la longitud de las palabras, aunque puede requerir ajustes significativos en la lógica del juego.

## Enlaces
- [Código del proyecto en GitHub](https://github.com/AngelChv/wordle)
- [Versión en Google Colab](https://github.com/AngelChv/wordle/blob/master/wordle.ipynb)

## Bibliografía
- [El libro de Python](https://ellibrodepython.com)
- [Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/)
- [Hello-Python de Mouredev](https://github.com/mouredev/Hello-Python)
- [Introducción a Rich](https://rich.readthedocs.io/en/stable/introduction.html)
