def calculador_notas():
    notas = input("Introduce la lista de notas separados por comas: ")
    lista = [int(x) for x in notas.split(",")]

    if all(nota >= 0 and nota <= 10 for nota in lista):
        pass
    else:
        raise ValueError("Notas fuera de rango entre 0 y 10")

    suma = sum(lista)
    media = suma / len(lista)
    minimo = min(lista)
    maximo = max(lista)

    for nota in lista:
        if nota < 5:
            print("Hay notas suspensas")
        else:
            pass

    return media, minimo, maximo


media, minimo, maximo = calculador_notas()
print("Media:", media)
print("Mínimo:", minimo)
print("Máximo:", maximo)