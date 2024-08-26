#Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
#cuando las letras que componen dicha palabra estén en orden alfabético, y False 
#en caso contrario.


palabra = input("Ingresar una palabra: ")

def es_abc(palabra):
    for i in range(len(palabra) - 1):
        if palabra[i] > palabra[i+1]:
            return False
    return True

print(es_abc(palabra))

#Ejemplos de ejecución:

#es_abc("abc") => True
#es_abc("cba") => True
#es_abc("hello") => False
#es_abc("edcba") => False
#es_abc("edcbaf") => False