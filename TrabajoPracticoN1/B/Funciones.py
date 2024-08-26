import time
from calendar import isleap

class Funciones:
    
    @staticmethod
    def anio_bisiesto(anio):
        return isleap(anio)

    @staticmethod
    def calcular_dias_mes(mes, anio_bisiesto):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9 ,11]:
            return 30
        elif mes == 2 and anio_bisiesto == True:
            return 29
        elif mes == 2 and anio_bisiesto == False:
            return 28

    @staticmethod
    def calcular_edad_en_dias(hora_local, anio_comienzo, anio_fin):
        dias = 0
        for a in range(anio_comienzo, anio_fin):
            dias += 366 if Funciones.anio_bisiesto(a) else 365
        
        for m in range(1, hora_local.tm_mon):
            dias += Funciones.calcular_dias_mes(m, Funciones.anio_bisiesto(hora_local.tm_year))
        
        dias += hora_local.tm_mday
        return dias
    
    @staticmethod
    def verificar_edad(edad):
        while edad.isdigit() == False:
            print(f"Error, {edad} no es un dígito.")
            edad = input("Ingrese su edad: ")
        return int(edad)