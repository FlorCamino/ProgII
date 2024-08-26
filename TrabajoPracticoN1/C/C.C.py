# Tal como sucede con la lógica proposicional, en Python muchas veces las 
# expresiones booleanas pueden ser simplificadas manteniendo el valor de 
# verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente 
# a and b. A continuación, intente simplificar las siguientes expresiones y 
# escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el 
# valor de verdad de las expresiones ya simplificadas:
# i. (a or b) or (b and c)
# ii. b and c or False
# iii. a and b or c or (b and a)
# iv. a == True or b == False

# Simplificaciones
# i. (a or b) or (b and c)
#     a or b or (b and c)
# ii. b and c or False
#     b and c
# iii. a and b or c or (b and a)
#      a and b or c
# iv. a == True or b == False
#     a or not b

def procesar_sentencias(a, b, c):
    print('\na=' + str(b) + ', b=' + str(b) + ', c=' + str(c))

    #Punto i.
    sentencia = (a or b) or (b and c)
    sentencia_reducida = a or b
    print(f"i. {sentencia} | {sentencia_reducida}")

    #Punto ii.
    sentencia = b and c or False
    sentencia_reducida = b and c
    print(f"ii. {sentencia} | {sentencia_reducida}")

    #Punto iii.
    sentencia = a and b or c or (b and a)
    sentencia_reducida = a and b or c
    print(f"iii. {sentencia} | {sentencia_reducida}")

    #Punto iv.
    sentencia = a == True or b == False
    sentencia_reducida = a or not b
    print(f"iv. {sentencia} | {sentencia_reducida}")

a=True
b=False
c=False
procesar_sentencias(a, b, c)

a=False
b=True
c=False
procesar_sentencias(a, b, c)

a=False
b=False
c=True
procesar_sentencias(a, b, c)

a=True
b=True
c=False
procesar_sentencias(a, b, c)

a=False
b=True
c=True
procesar_sentencias(a, b, c)

a=True
b=False
c=True
procesar_sentencias(a, b, c)

a=True
b=True
c=True
procesar_sentencias(a, b, c)

a=False
b=False
c=False
procesar_sentencias(a, b, c)