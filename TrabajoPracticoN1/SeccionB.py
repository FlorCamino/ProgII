# A continuación, se presenta el código de un programa que,
# ante la edad ingresada por el usuario, este presenta el equivalente en días,
# meses y años. Se solicita al alumno que lo refactorice de manera tal que:

# a. Se elimine la sentencia if / else de la función anio_bisiesto.
# b. Las múltiples sentencias if la función dia_mes utilicen la cláusula
# in en lugar de varias cláusulas or.
# c. Se agregue una sentencia que valide que la edad ingresada por el usuario
# es numérica.
# d. Se agregue una función que encapsule el cálculo del equivalente de la edad
# en días y que tome como parámetros las variables hora_local, anio_comienzo y
# anio_fin.
# e. Todas las funciones sean transportadas a un archivo auxiliar de funciones
# llamado funciones.py, y este sea importado desde el programa principal.

import time
from Funciones import Funciones

# Ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Verifico y converto la edad ingresada
anios = Funciones.verificar_edad(edad)

# Seteo de variables
hora_local = time.localtime(time.time())  
anio_comienzo = hora_local.tm_year - anios  
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon

# Calculo los días
dias = Funciones.calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin)

# Muestro los resultados
print(f"{nombre}, has vivido con {edad} años: ")
print(f"{dias} días - {meses} meses - {anios} años")