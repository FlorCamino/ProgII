#Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
#que tome ambas como parámetros e imprima dos listas, cada una con:
#i. Los elementos en común, en orden inverso.
#ii. Los elementos no comunes, en orden alfabético.
#El programa debería arrojar el siguiente resultado:
#listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
#['c', 'b']
#['a', 'e', 'd']"""

lista1 = ["a", "b", "d", "e"]
lista2 = ["b", "f", "e", "g", "h"]

def listas_diferencia(lista1, lista2):
    comunes = []
    no_comunes = []
    for i in lista1:
        if i in lista2:
            comunes.append(i)
        else:
            no_comunes.append(i)
    for i in lista2:
        if i not in lista1:
            no_comunes.append(i)
    print(comunes[::-1])
    print(sorted(no_comunes))

listas_diferencia(lista1, lista2)