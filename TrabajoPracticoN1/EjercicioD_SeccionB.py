#Se agregue una función que encapsule el cálculo del equivalente de la edad
# en días y que tome como parámetros las variables hora_local, anio_comienzo
# y anio_fin.

import time
from calendar import isleap

# Calcular si es un año bisiesto
def anio_bisiesto(anio):
    return isleap(anio)

# Calcular el número de días de cada mes
def calcular_dias_mes(mes, anio_bisiesto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if anio_bisiesto else 28

# Calcular la edad en días
def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
    dias = 0
    for a in range(anio_comienzo, anio_fin):
        dias += 366 if anio_bisiesto(a) else 365
    
    for m in range(1, hora_local.tm_mon):
        dias += calcular_dias_mes(m, anio_bisiesto(hora_local.tm_year))
    
    dias += hora_local.tm_mday
    return dias

# Ingreso de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

# Seteo inicial de variables
hora_local = time.localtime(time.time())
anios = int(edad)
anio_comienzo = int(hora_local.tm_year) - anios
anio_fin = anio_comienzo + anios
meses = anios * 12 + hora_local.tm_mon

# Calcular los días
dias = calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin)

# Imprimir la edad del usuario
print(f"La edad de {nombre} es {anios} años o {meses} meses o {dias} días")