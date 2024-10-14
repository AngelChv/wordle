# pip install wordfreq
import wordfreq
import random

def obtener_palabra_wordfreq():
    palabras = wordfreq.top_n_list('es', 1000)  # Obtén las 1000 palabras más comunes
    palabras_5_letras = [p for p in palabras if len(p) == 5]
    return random.choice(palabras_5_letras)

# Ejemplo de uso
palabra_wordfreq = obtener_palabra_wordfreq()
print(f"Palabra aleatoria (wordfreq): {palabra_wordfreq}")
