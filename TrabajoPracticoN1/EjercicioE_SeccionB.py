import time
from Funciones import Funciones

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
dias = Funciones.calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin)