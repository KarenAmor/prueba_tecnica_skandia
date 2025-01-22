def invertir_palabras(cadena):
    # Convertir la cadena en una lista de palabras
    palabras = cadena.split()
    # Invertir el orden de las palabras
    palabras_invertidas = palabras[::-1]
    # Unir las palabras invertidas en una nueva cadena
    return ' '.join(palabras_invertidas)

# Ejemplo de uso
entrada = "el amor mas grande del planeta"
salida = invertir_palabras(entrada)
print(salida)