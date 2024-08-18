# Escribir un programa que resuelva la secuencia de Fibonacci a pedido del usuario.
# Deberá codificar una función fibonacci(numero), 
# cuyo parámetro numero debe ser ingresado por el usuario y su tipo,
# al igual que en el ejercicio anterior, validado. 
# La función debe encargarse de calcular la secuencia para dicho número. 
def fibonacci(numero): 
    secuencia = [0, 1]
    while secuencia[-1] < numero:
        siguiente = secuencia[-1] + secuencia[-2]
        if siguiente > numero:
            break
        secuencia.append(siguiente)
    return secuencia
def validar_entrada(mensaje):
    """
    Valida la entrada del usuario para que sea un número entero positivo.
    """
    while True:
        try:
            entrada = int(input(mensaje))
            if entrada > 0:
                return entrada
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Programa principal
if __name__ == "__main__":
    numero = validar_entrada("Ingresar el número para calcular la secuencia de Fibonacci: ")
    secuencia_fibonacci = fibonacci(numero)
    print(f"La secuencia resultante de Fibonacci hasta {numero} es: {secuencia_fibonacci}")