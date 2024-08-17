# f. Un portal web requiere un formulario de alta de usuario donde se ingrese, 
# mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, 
# una función contrasena_valida(contrasena) que devuelva True en caso de superar
# las siguientes validaciones sobre la contraseña proporcionada por el usuario: 
#     i. Longitud entre 6 y 20 caracteres. 
#     ii. Debe contener al menos un número. 
#     iii. Debe contener al menos dos mayúsculas. 
#     iv. Debe contener al menos un carácter especial. 
#     v. No puede contener espacios.  

# La salida esperada es la siguiente: 
#     abc.123 es válida:      False 
#     Abc.123 es válida:      False 
#     AbC.123 es válida:      True 
#     AbC.1 23 es válida:     False 
#     ÁbC.123 es válida:      False  
    
# Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y otros)
# debe hacerse uso de la librería re: - https://docs.python.org/es/3/library/re.html -
# https://relopezbriega.github.io/blog/2015/07/19/expresiones-regularescon-python/ - 
# Para buscar caracteres especiales, puede utilizarse la siguiente expresión
# [$&+,:;=?@#|<>.^*()%!-]

import re

def contrasena_valida(contrasena):
    # i. Longitud entre 6 y 20 caracteres.
    if not 6 <= len(contrasena) <= 20:
        print("La contraseña ingresada no tiene una longitud entre 6 y 20 caracteres")
        return False

    # ii. Debe contener al menos un número.
    if not re.search(r'\d', contrasena):
        print("La contraseña ingresada no contiene el valor numérico obligatorio")
        return False

    # iii. Debe contener al menos dos mayúsculas.
    if len(re.findall(r'[A-Z]', contrasena)) < 2:
        print("La contraseña ingresada no contiene al menos dos mayúsculas obligatorias")
        return False

    # iv. Debe contener al menos un carácter especial.
    if not re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        print("La contraseña ingresada no contiene al menos un carácter especial obligatorio")
        return False

    # v. No puede contener espacios.
    if re.search(r'\s', contrasena):
        print("La contraseña ingresada no puede contener espacios")
        return False

    return True

username = input("Por favor, ingrese su usuario: ")
password = input("Por favor, ingrese su contraseña: ")
print("Debe contener: ")
print("- Longitud entre 6 y 20 caracteres")
print("- Debe contener al menos un número")
print("- Debe contener al menos dos mayúsculas")
print("- Debe contener al menos un carácter especial")
print("- No puede contener espacios")

es_valida = contrasena_valida(password)

while not es_valida:
    password = input("Vuelva a ingresar la contraseña: ")
    es_valida = contrasena_valida(password)

print("El usuario ingresado es: ", username)
print("La contraseña válida ingresada es: ", password)