def clasificador(lista):
    pares = []
    impares = []
    negativos = []

    for numero in lista:
        if numero < 0:
            negativos.append(numero)
        elif numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        
    return pares, impares, negativos

lista = [10, -3, 5, 8, -1, 7, 2, -6, 4, 9]

pares, impares, negativos = clasificador(lista)

print("Números pares:", pares)
print("Números impares:", impares)
print("Números negativos:", negativos)