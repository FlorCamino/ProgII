# Escriba un procedimiento procesar_palabras(entrada) que acepte una 
# secuencia de palabras separadas por coma, las ordene y las imprima. 
# Suponiendo que la entrada provista al programa es la siguiente:
# te,felicito,que,bien,actuas
# La salida esperada es:
# actuas,bien,felicito,que,te

def procesar_palabras(entrada):
    palabras = entrada.split(",")
    palabras.sort()
    for palabra in palabras:
        print(palabra, end=", ")
    print()
    return None

procesar_palabras("te,felicito,que,bien,actuas")

# Resultado esperado: actuas, bien, felicito, que, te