# Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo que numero = 10: 1+2+3+4+5+6+7+8+9+10
# El programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro número
# ii. Debe validarse que el dato ingresado por el usuario corresponda a un dígito, y no a otro tipo de dato como un carácter
# iii. El cálculo debe realizarse usando algún tipo de bucle - LISTO

def suma(numero):
    # Sección de verificación
    while numero.isdigit() == False:
        print(f"Error, {numero} no es un dígito, por favor escriba un dígito")
        numero = input("Por favor escriba un número a continuación: ")
    numero = int(numero)
    
    # Sección de sumatoria
    resultado_suma = 0
    for i in range(1, numero + 1):
        resultado_suma += i
    print(f"El resultado de la suma es: {resultado_suma}")
        
numero = input("Dime un número cualquiera: ")

suma(numero)