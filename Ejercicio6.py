def inventario_personajes(personajes):
    humanos = []
    criaturas = []

    for nombre, tipo in personajes.items():
        if tipo == "humano":
            humanos.append(nombre)
        else:
            criaturas.append(nombre)

    return humanos, criaturas

personajes = {
    "Ana": "humano",
    "Luis": "humano",
    "Marta": "humano",
    "Draco": "criatura",
    "Fénix": "criatura",
    "Orco": "criatura",
    "Sirena": "criatura"
}

humanos, criaturas = inventario_personajes(personajes)

print("Humanos: ",humanos)
print("Criaturas: ",criaturas)